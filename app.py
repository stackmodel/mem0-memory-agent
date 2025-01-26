import os
import streamlit as st
from mem0 import MemoryClient
from autogen import ConversableAgent

def main():
      
    config_list_gemini= [{
        "model": "gemini-1.5-flash-latest",
        "api_key": os.getenv('GOOGLE_API_KEY'),
        "api_type": "google"
    }]
    
    agent = ConversableAgent(
        "chatbot",
        llm_config={"config_list": config_list_gemini},
        code_execution_config=False,
        function_map=None,
        human_input_mode="NEVER",
    )

    memory = MemoryClient(api_key=os.getenv('API_KEY'))
    def generate_reply(prompt):
        return agent.generate_reply(messages=[{"content": prompt, "role": "user"}])

    conversation = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to the Precision Medicine Support Center. How can I assist you today?"
        },
        {
            "role": "user",
            "content": "I’m curious about precision medicine and how it can be applied to cancer treatment."
        },
        {
            "role": "assistant",
            "content": "Thanks for reaching out! Precision medicine in cancer care involves tailoring treatments based on the specific genetic changes in your cancer cells. This helps doctors choose the most effective treatments and avoid ones that might not work. Could you share more about your concerns or your family history with cancer?"
        },
        {
            "role": "user",
            "content": "I have a family history of breast cancer, and I’m wondering if precision medicine could help with early detection or treatment options."
        },
        {
            "role": "assistant",
            "content": "Thanks for sharing that. With your family history, precision medicine can help assess your risk of breast cancer through genetic testing. It can also provide insights into which treatments might be more effective for you if you were diagnosed. Testing for genetic mutations, like BRCA1 or BRCA2, could help guide early screening and preventive options. Would you like to learn more about how genetic testing works for breast cancer?"
        },
        {
            "role": "user",
            "content": "Yes, I’d like to know more about genetic testing for breast cancer."
        },
        {
            "role": "assistant",
            "content": "Genetic testing for breast cancer usually involves a blood or saliva sample. The test looks for specific gene mutations that could increase your risk, like BRCA1 or BRCA2. If you have one of these mutations, your doctor might recommend earlier screening or preventive treatments to reduce your cancer risk. It can also help your doctor make decisions about the most effective treatments if you're diagnosed. Would you like help setting up a genetic counseling appointment to discuss this further?"
        },
        {
            "role": "user",
            "content": "Yes, I’d like to schedule an appointment."
        },
        {
            "role": "assistant",
            "content": "Great! I can help arrange that for you. Would you prefer a virtual or in-person consultation?"
        },
        {
            "role": "user",
            "content": "A virtual consultation would be most convenient for me."
        },
        {
            "role": "assistant",
            "content": "Got it! I’ll schedule your virtual consultation. What time works best for you tomorrow?"
        },
        {
            "role": "user",
            "content": "Tomorrow afternoon would be ideal."
        },
        {
            "role": "assistant",
            "content": "Your virtual consultation is scheduled for tomorrow afternoon. You’ll receive an email with the confirmation and a link to join the session. If you have any questions before then, feel free to reach out!"
        },
        {
            "role": "user",
            "content": "Thank you so much for your help!"
        },
        {
            "role": "assistant",
            "content": "You're very welcome! We look forward to helping you on your precision medicine journey. Have a wonderful day!"
        }
    ]


    if 'conversation_added' not in st.session_state:
        # Add the initial conversation only once
        st.session_state.memory = memory
        memory.add(messages=conversation, user_id="customer_service_bot")
        st.session_state.conversation_added = True

    st.title("Long Term Memory + AI Agent")
    st.header("(Mem0 + AutoGen)")
    # st.subheader("Precision Medicine Consulting AI Agent")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Retrieve relevant memories for the user input
        relevant_memories = st.session_state.memory.search(prompt, user_id="customer_service_bot")
        relevant_memories_text = ""
        if relevant_memories:
            relevant_memories_text = '\n'.join(mem["memory"] for mem in relevant_memories)

        # Update memory with the new user message
        st.session_state.memory.add(messages=prompt, user_id="customer_service_bot")
        
        # Create a prompt for the assistant with memories
        prompt_w_mem = f"""Answer the user question considering the memories. Keep answers clear and concise.
        Memories:
        {relevant_memories_text}
        
        Question: {prompt}
        """
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response from the bot
        response = generate_reply(prompt_w_mem)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response['content']})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response['content'])

if __name__ == '__main__':
    main()
