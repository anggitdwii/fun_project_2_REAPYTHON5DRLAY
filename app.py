import streamlit as st
import requests
import json

# Custom CSS untuk styling chat bubble
st.markdown("""
<style>
/* User message - kanan */
.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 14px 18px;
    border-radius: 18px 18px 4px 18px;
    margin-left: auto;
    margin-right: 8px;
    max-width: 80%;
}

/* Assistant message - kiri */
.stChatMessage:has([data-testid="stChatMessageAvatarAssistant"]) .stMarkdown {
    background: #374151;
    padding: 14px 18px;
    border-radius: 18px 18px 18px 4px;
    margin-left: 8px;
    max-width: 80%;
}

/* Text color */
.stChatMessage p, .stChatMessage span {
    color: white !important;
}

/* Spasi antar pesan */
.stChatMessage {
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

def get_ai_response(messages, model, api_key):
    """Fungsi untuk mendapatkan respons dari API"""
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "model": model,
                "messages": messages,
                "max_tokens": 1000,
                "temperature": 0.7,
            }
        )
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"

# Judul aplikasi
st.title("🎯 Nana AI Chatbot")

# Sidebar untuk pengaturan
with st.sidebar:
    st.header("⚙️ Pengaturan")
    
    api_key = st.text_input("API Key OpenRouter", 
                          type="password",
                          help="Masukkan API key dari OpenRouter")
    
    st.markdown("---")
    
    model = st.selectbox(
        "Pilih Model AI:",
        [
            "mistralai/mistral-7b-instruct:free",
            "deepseek/deepseek-chat-v3-0324:free",
            "meta-llama/llama-3.3-70b-instruct:free"
        ],
        index=0
    )
    
    if st.button("🧹 Hapus Chat"):
        st.session_state.messages = []
        st.rerun()

# Inisialisasi chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan pesan sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input pengguna
if prompt := st.chat_input("Ketik pesan..."):
    # Cek API key
    if not api_key:
        st.warning("⚠️ Masukkan API Key di sidebar terlebih dahulu!")
        st.stop()
    
    # Tambahkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate respons AI
    with st.chat_message("assistant"):
        with st.spinner("Mengetik..."):
            response = get_ai_response(st.session_state.messages, model, api_key)
            
            if response:
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
