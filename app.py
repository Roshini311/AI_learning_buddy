import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Check for API Key
API_KEY = os.getenv("OPENAI_API_KEY")
if API_KEY:
    client = OpenAI(api_key=API_KEY)
    USING_MOCK = False
else:
    USING_MOCK = True

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PROFESSIONAL UI ---
st.markdown("""
<style>
    /* Styling chat messages */
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    
    /* Disclaimer text styling */
    .disclaimer-text {
        font-size: 0.8rem;
        color: #888;
        margin-top: 20px;
        border-top: 1px solid #ddd;
        padding-top: 10px;
    }
    
    /* Metric styling */
    div[data-testid="stMetricValue"] {
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add initial greeting
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi there! 👋 I'm Algo Andy, your friendly AI Learning Buddy. I'm here to help you master software engineering concepts. What would you like to learn today?"
    })
if "interactions_count" not in st.session_state:
    st.session_state.interactions_count = 0
if "quizzes_taken" not in st.session_state:
    st.session_state.quizzes_taken = 0
if "current_topic" not in st.session_state:
    st.session_state.current_topic = "Binary Search"
if "learner_level" not in st.session_state:
    st.session_state.learner_level = "Beginner"

# --- HELPER FUNCTIONS ---
def get_ai_response(prompt):
    """Fetches response from OpenAI or returns a mock response if no API key is provided."""
    if USING_MOCK:
        time.sleep(1) # Simulate network delay
        # Mock responses based on keywords in prompt
        prompt_lower = prompt.lower()
        if "explain" in prompt_lower:
            if st.session_state.current_topic == "Binary Search":
                return f"""**Mock Mode**: Let's break down **{st.session_state.current_topic}** into simple terms! 

Imagine you have a list of numbers. If I asked you to find the number `7`, you could look at every single number one by one until you find it. That is called *Linear Search*. It works, but if the list has a million numbers, it would take forever!

**Binary Search** is a much faster way to find a target, but it has one strict rule: **The list MUST be sorted** (like 1, 2, 3, 4...). 

Here is how it works:
1. **Find the middle:** You start by looking directly at the middle element of the sorted list.
2. **Compare:** You check if your target is higher, lower, or equal to that middle element.
3. **Discard half:** Because the list is sorted, if your target is *higher* than the middle, you instantly know it cannot be in the left half. You can completely throw away the left half of the list!
4. **Repeat:** You then take the remaining right half, find its middle, and repeat the process until you find your target.

By cutting the problem in half every single step, Binary Search is incredibly fast! Does this make sense for your {st.session_state.learner_level} level?"""
            else:
                return f"**Mock Mode**: {st.session_state.current_topic} is a core computer science concept. To understand it, we break it down into its fundamental rules and logic. (Please set up an OpenAI API key to dynamically explain topics other than Binary Search!)"
        
        elif "real-life example" in prompt_lower or "example" in prompt_lower:
            if st.session_state.current_topic == "Binary Search":
                return f"""**Mock Mode**: Here is a great real-life analogy for **{st.session_state.current_topic}**:

Imagine you are looking up the word "Algorithm" in a physical, printed dictionary. 
- Would you start at page 1 and read every single word? No! 
- You would open the dictionary right to the middle. 
- Let's say you open to words starting with "M". Since "A" comes before "M" in the alphabet, you know that "Algorithm" MUST be in the left half of the book. 
- You can completely ignore the entire right half of the dictionary! 
- Then, you open the middle of the left half, and repeat this process.

You are performing Binary Search in real life by constantly halving your search space!"""
            else:
                 return f"**Mock Mode**: A real-life example of {st.session_state.current_topic}. Imagine you are managing a library system... (Set up an OpenAI API key for dynamic examples!)"
        
        elif "quiz" in prompt_lower:
            if st.session_state.current_topic == "Binary Search":
                return f"""**Mock Mode**: Let's test your knowledge on **{st.session_state.current_topic}**! 

1. What is the one strict requirement for a list before you can use Binary Search?
   A) It must have an even number of items
   B) It must be sorted
   C) It must contain only integers

2. In our dictionary analogy, what is the first step you take?
   A) Read the first page
   B) Open to the middle
   C) Read the last page

3. If the target item is LESS than the middle item, which half of the array do you discard?
   A) The left half
   B) The right half
   C) You discard the whole array

4. True or False: Binary Search is much faster than checking items one by one.
   A) True
   B) False

5. What happens if you try to use Binary Search on an unsorted array?
   A) It works normally
   B) It crashes your computer
   C) It will likely fail to find the target

Reply with your answers (e.g., "1B, 2B, 3B, 4A, 5C") for evaluation!"""
            else:
                return f"**Mock Mode**: Here is a 5-question quiz on {st.session_state.current_topic}... (Please set up an API key to generate dynamic quizzes!)"
        
        elif "evaluate" in prompt_lower or "evaluate answer" in prompt_lower:
            st.session_state.quizzes_taken += 1
            return """**Mock Mode**: Let's check your answers! 

1. **B** - Correct! The array must be sorted.  
2. **B** - Correct! You open to the middle.  
3. **B** - Correct! If the target is LESS than the middle, you keep the left half and discard the right half.  
4. **A** - Correct! It is much faster because it cuts the problem in half every step.  
5. **C** - Correct! It will fail because the logic relies on the items being in order.  

Great effort! Keep up the good work!"""
        else:
            return "**Mock Mode**: I am currently running without an API key, so I have limited responses. Please try using the quick action buttons in the sidebar for detailed examples and quizzes!"
            
    else:
        try:
            # Construct system prompt based on persona and selected options
            system_prompt = f"""
            You are Algo Andy, an encouraging, friendly, and expert AI tutor for software engineering concepts.
            Your current topic is: {st.session_state.current_topic}.
            The learner's level is: {st.session_state.learner_level}.
            Always explain things clearly, use analogies, and be supportive.
            """
            
            api_messages = [{"role": "system", "content": system_prompt}]
            # Only send the last 10 messages for context window management
            for msg in st.session_state.messages[-10:]:
                api_messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Add the current prompt
            api_messages.append({"role": "user", "content": prompt})
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=api_messages,
                temperature=0.7,
                max_tokens=800
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"An error occurred while connecting to the AI: {str(e)}"

def add_message_and_respond(user_prompt, display_prompt=None):
    """Adds user message to history, gets AI response, and updates history."""
    st.session_state.interactions_count += 1
    
    # Sometimes we want to trigger an action (like "Explain") but display it nicely
    msg_to_display = display_prompt if display_prompt else user_prompt
    
    st.session_state.messages.append({"role": "user", "content": msg_to_display})
    
    with st.spinner("Algo Andy is thinking..."):
        ai_response = get_ai_response(user_prompt)
        
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

def clear_chat():
    """Resets the chat history."""
    st.session_state.messages = []
    st.session_state.interactions_count = 0
    st.session_state.quizzes_taken = 0
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Chat cleared! Let's start fresh. What would you like to learn about {st.session_state.current_topic}?"
    })

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Topic Selector
    topics = ["Binary Search", "SQL Joins", "Object-Oriented Programming", "Linked Lists", "Python Functions"]
    st.session_state.current_topic = st.selectbox("Select Topic", topics, index=0)
    
    # Learner Level Selector
    levels = ["Beginner", "Intermediate", "Advanced"]
    st.session_state.learner_level = st.selectbox("Learner Level", levels, index=0)
    
    st.divider()
    
    # Quick Actions
    st.subheader("🚀 Quick Actions")
    if st.button("📖 Explain Topic", use_container_width=True):
        add_message_and_respond(f"Explain the topic {st.session_state.current_topic} in simple language suitable for a {st.session_state.learner_level}.", "Please explain the topic to me.")
        st.rerun()
        
    if st.button("💡 Real-Life Example", use_container_width=True):
        add_message_and_respond(f"Give me a real-life analogy or example to understand {st.session_state.current_topic}.", "Can you give me a real-life example?")
        st.rerun()
        
    if st.button("📝 Generate Quiz", use_container_width=True):
        add_message_and_respond(f"Generate a 5-question multiple choice quiz on {st.session_state.current_topic}.", "I'm ready for a quiz!")
        st.rerun()
        
    if st.button("✅ Evaluate Answer", use_container_width=True):
        # We prompt the user to type their answers in the chat
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "Please type your quiz answers in the chat box below, and I'll evaluate them!"
        })
        st.rerun()
        
    st.button("🗑️ Clear Conversation", on_click=clear_chat, type="secondary", use_container_width=True)
    
    st.divider()
    
    # Progress Tracker
    st.subheader("📊 Your Progress")
    col1, col2 = st.columns(2)
    col1.metric("Messages", st.session_state.interactions_count)
    col2.metric("Quizzes", st.session_state.quizzes_taken)
    
    # Responsible AI Disclaimer
    st.markdown("""
        <div class="disclaimer-text">
        <strong>🛡️ Responsible AI Notice:</strong><br>
        AI-generated responses may occasionally contain inaccuracies or hallucinations. Please verify important technical information using trusted sources or official documentation.
        </div>
    """, unsafe_allow_html=True)
    
    if USING_MOCK:
        st.warning("⚠️ Running in Mock Mode. Set OPENAI_API_KEY in .env for live AI responses.")

# --- MAIN CHAT INTERFACE ---
st.title("🎓 AI Learning Buddy")
st.markdown(f"**Current Topic:** `{st.session_state.current_topic}` | **Level:** `{st.session_state.learner_level}`")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your question or answers here..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to session state and get AI response
    add_message_and_respond(prompt)
    
    # Rerun to update the UI with the new assistant message
    st.rerun()
