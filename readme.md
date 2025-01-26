**Adding Long Term Memory to Agent**  

![app_screenshot](https://github.com/user-attachments/assets/bb7d2a06-b97e-4a42-aa6c-e7866f5e66ac)

This code demonstrates the creation of a personalized AI Agent for providing support in the context of precision medicine. The Agent utilizes memory management to provide relevant responses based on prior user interactions, offering a more personalized and context-aware experience.

**Setup Instructions**

1. Clone the repository
```
git clone https://github.com/stackmodel/mem0-memory-agent.git
cd mem0-memory-agent
```
2. install Dependencies:

    - Make sure you have Python 3.7 or higher installed. Then, create a virtual environment and install the dependencies:
      
      ```
      python -m venv env
      source env/bin/activate  # For Linux/macOS
      .\env\Scripts\activate   # For Windows
      pip install -r requirements.txt
      ```
3. Rename .env.example to .env file and populate the google gemini api key and Mem0 api key.
   You can obtain your
    Google API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    Mem0 API Key from [Mem0 Platform](https://app.mem0.ai/login)
   

4. Run the app using the following command: ```streamlit run app.py```
   launch the app in your browser at http://localhost:8501


**Key features and concepts in the code**

1. Memory Integration (Mem0):

The MemoryClient is used to store and retrieve past user interactions, allowing the agent to remember the user's context across sessions.
This is especially useful for maintaining a consistent conversation flow and offering answers based on previous user inputs.

2. Conversable Agent (AutoGen):

The ConversableAgent is a custom AI model that handles the generation of responses. The Agent is configured to use a specific model (gemini-1.5-flash-latest) and operates in a "never" human input mode, meaning it doesn't ask for further clarifications from users directly, but provides responses based on prior interactions.

3. Streamlit for Frontend:

The code uses Streamlit to create a web-based interface where users can interact with the Agent.
Users can enter prompts (questions), and the Agent responds in real-time, showing the conversation history.

4. Precision Medicine Consultation:

The initial conversation focuses on providing information about precision medicine in cancer care. The Agent uses natural language to engage the user, explaining complex medical topics like genetic testing for cancer and offering to schedule appointments.

5. Memory Update:

The agent dynamically adds new messages to memory and retrieves relevant past interactions whenever the user asks a new question. This helps the agent tailor its responses based on the user’s past input.

**Code Flow**

![mem0_f1](https://github.com/user-attachments/assets/e0e2c34c-9af9-4937-a68e-9ca818cd834d)

    1️⃣ User Submits a Question via the Streamlit chat interface. (can also be voice activated assistant)
    2️⃣ Mem0 Searches for Relevant Memories:
        If relevant memories exist, they’re retrieved; if not, Mem0 decides whether to add new ones based on the query.
    3️⃣ Query & Memories Sent to the AI Agent for further processing.
    4️⃣ Agent Utilizes a Large Language Model (LLM):
        In this example, we use Gemini-1.5-flash-latest to craft thoughtful responses, combining both the user’s query and relevant contextual info.
    5️⃣ Response Displayed to the user via the Streamlit interface.

**TL;DR**

Chatbot vs Agent

At a coffee shop, Chatbot follows a fixed menu, handling only predefined orders. AI Agent, however, can suggest custom drinks, like a spicy cinnamon latte, because it reasons and adapts based on knowledge.
