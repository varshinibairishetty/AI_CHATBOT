import streamlit as st
import requests

# Page Config with a dark/modern theme feel
st.set_page_config(page_title="🤖 Agentic AI Hub", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for a Polished Look ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white;
        font-weight: bold;
        border: none;
    }
    .stTextArea textarea { border-radius: 15px; }
    .agent-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #1e2130;
        border: 1px solid #3e4150;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Configuration ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=80)
    st.title("AI ChatBot")
    st.divider()
    
    provider = st.radio("⚙️ AI Provider", ("Groq", "Gemini"))
    
    if provider == "Groq":
        selected_model = st.selectbox("🧠 Model", ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"])
    
    else:
        selected_model = st.selectbox("🧠 Model", ["gemini-1.5-flash", "gemini-1.5-pro"])

    allow_web_search = st.toggle("🌐 Enable Web Search", value=False)
    

# --- Main Interaction Area ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🛠️ Brain Setup")
    with st.container():
        system_prompt = st.text_area(
            "Define Persona:", 
            height=150, 
            placeholder="e.g. You are a Senior Python Developer who gives concise code solutions.",
            help="This sets the personality of your AI Agent."
        )

with col2:
    st.subheader("💬 Chat Interface")
    user_query = st.text_area("What's on your mind?", height=150, placeholder="Type your message here...")
    
    if st.button("🚀 Launch Agent"):
        if not user_query.strip():
            st.warning("Please enter a query first!")
        else:
            API_URL = "http://127.0.0.1:9999/chat"
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt if system_prompt else "You are a helpful AI assistant.",
                "messages": [user_query],
                "allow_search": allow_web_search
            }

            with st.status("🔗 Connecting to Brain...", expanded=True) as status:
                try:
                    response = requests.post(API_URL, json=payload)
                    if response.status_code == 200:
                        data = response.json()
                        status.update(label="✅ Response Received!", state="complete", expanded=False)
                        
                        # Displaying response in a nice card
                        st.markdown("### 🤖 Agent Response")
                        st.success(data.get("reply", "No reply received."))
                    else:
                        st.error(f"Backend Error: {response.status_code}")
                except Exception as e:
                    st.error(f"Connection Failed! Is backend.py running? \n\n {e}")

