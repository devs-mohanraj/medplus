import streamlit as st
from interface import process_query

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.set_page_config(
    page_title="Medplus",
    page_icon="🔴",
    layout="wide"
)

st.markdown("""
    <style>
    .main-container {
        display: flex;
        flex-direction: column;
        height: 100vh;
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        padding-bottom: 80px;
    }
    
    .chat-container {
        flex: 1;
        overflow-y: auto;
        padding: 2rem;
        margin-bottom: 0;
        height: calc(100vh - 280px);
        overflow-x: hidden;
    }
    
    .input-container {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 800px;
        max-width: 100%;
        background-color: white;
        padding: 1rem 2rem;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        border-top: 1px solid #eee;
        z-index: 1000;
    }
    
    .chat-message {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1.5rem;
        animation: fadeIn 0.5s ease-in;
    }
    
    .user-message {
        justify-content: flex-end;
    }
    
    .message-bubble {
        padding: 1rem 1.5rem;
        border-radius: 20px;
        max-width: 80%;
        font-size: 1.1rem;
        line-height: 1.5;
    }
    
    .user-bubble {
        background-color: #9747FF;
        color: white;
        border-bottom-right-radius: 5px;
        margin-left: 20px;
    }
    
    .assistant-bubble {
        background-color: #f0f2f6;
        border-bottom-left-radius: 5px;
        margin-right: 20px;
    }
    
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }
    
    .user-avatar {
        background-color: #9747FF;
        color: white;
    }
    
    .assistant-avatar {
        background-color: #f0f2f6;
        color: #1a1a1a;
    }
    
    .input-container {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 800px;
        max-width: 100%;
        background-color: white;
        padding: 1rem 2rem;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        border-top: 1px solid #eee;
        z-index: 1000;
    }
    
    .stTextInput>div>div>input {
        font-size: 1.1rem !important;
        padding: 1rem 1.5rem !important;
        border-radius: 25px !important;
        border: 2px solid #e0e0e0 !important;
        background-color: #ffffff;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #9747FF !important;
        box-shadow: 0 0 0 1px #9747FF !important;
    }
    
    .stButton>button {
        border-radius: 25px !important;
        background-color: #9747FF !important;
        color: white !important;
        padding: 0.5rem 2rem !important;
        font-size: 1.1rem !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background-color: #8438E3 !important;
        transform: translateY(-1px);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .custom-title {
        font-size: 2.5rem !important;
        font-weight: bold;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .custom-subtitle {
        font-size: 1.3rem !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

left_col, main_col, right_col = st.columns([1, 3, 1])

with main_col:
    st.markdown('<p class="custom-title">Medplus</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-subtitle">Your AI assistant for diabetes-related questions</p>', unsafe_allow_html=True)
    
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            
            message_style = "user-message" if role == "user" else "assistant-message"
            avatar = "👤" if role == "user" else "🤖"
            st.markdown(f"""
                <div class="chat-message {message_style}">
                    <div class="avatar {role}-avatar">{avatar}</div>
                    <div class="message-bubble {role}-bubble">
                        <div class="message-header">{'You' if role == 'user' else 'DiabetesCare Bot'}</div>
                        <div class="message-content">{content}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        input_col, button_col = st.columns([6, 1])
        
        with input_col:
            user_question = st.text_input("", 
                placeholder="Type your diabetes-related question here...", 
                key="user_input",
                label_visibility="collapsed")
        
        with button_col:
            send_button = st.button("Send", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
            
        if send_button and user_question:
            try:
                st.session_state.messages.append({"role": "user", "content": user_question})
                
                with st.spinner('Thinking...'):
                    response = process_query(user_question)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                st.rerun()
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with st.sidebar:
    st.markdown("### 🔍 Quick Tips")
    st.markdown("""
    **Try asking about:**
    - Symptoms of diabetes
    - Risk factors
    - Diagnosis methods
    - Treatment options
    - Prevention strategies
    """)
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("""
    <div style='font-size: 0.9rem; text-align: center; color: #888;'>
    Powered by Together AI and LangChain<br>
    🔒 Your conversations are private
    </div>
    """, unsafe_allow_html=True)
