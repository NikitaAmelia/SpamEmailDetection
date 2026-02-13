import streamlit as st
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Custom CSS untuk tema silver abu-abu
st.markdown("""
    <style>
    /* Background utama */
    .stApp {
        background: #d5d5d5;
    }
    
    /* Header styling */
    .main-header {
        background: #a8a8a8;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        text-align: center;
        margin-bottom: 2rem;
        border: 2px solid #8a8a8a;
    }
    
    .main-header h1 {
        color: #2c2c2c;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
    }
    
    .main-header p {
        color: #4a4a4a;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    /* Card container */
    .card {
        background: #e8e8e8;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        margin: 1rem 0;
        border: 1px solid #b8b8b8;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background-color: #ffffff !important;
        border: 2px solid #b0b0b0 !important;
        border-radius: 10px !important;
        color: #2c2c2c !important;
        font-size: 1rem !important;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #808080 !important;
        box-shadow: 0 0 0 2px rgba(128, 128, 128, 0.2) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: #909090 !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        padding: 0.75rem 2rem !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background: #707070 !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3) !important;
        transform: translateY(-2px);
    }
    
    /* Result box */
    .result-box {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1.5rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        border: 2px solid #c0c0c0;
    }
    
    .result-spam {
        color: #c41e3a;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    .result-ham {
        color: #2d7d2d;
        font-size: 1.8rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    .proba-text {
        background: #d8d8d8;
        color: #2a2a2a;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        border: 1px solid #b0b0b0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Warning styling */
    .stAlert {
        background-color: #f0f0f0 !important;
        border-left: 4px solid #909090 !important;
        border-radius: 8px !important;
    }
    
    /* Info box */
    .info-box {
        background: #c0c0c0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #808080;
        margin: 1rem 0;
        color: #2a2a2a;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #5a5a5a;
        padding: 1.5rem;
        margin-top: 2rem;
        font-size: 0.9rem;
        border-top: 2px solid #b0b0b0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>📧 Spam Email Classification</h1>
        <p>Deteksi email spam dengan teknologi Machine Learning</p>
    </div>
""", unsafe_allow_html=True)

# Info box
st.markdown("""
    <div class="info-box">
        <strong>ℹ️ Cara Penggunaan:</strong><br>
        1. Masukkan teks email yang ingin Anda periksa<br>
        2. Klik tombol "🔍 Analisis Email"<br>
        3. Sistem akan menampilkan hasil prediksi
    </div>
""", unsafe_allow_html=True)

# Input area dalam card
# st.markdown('<div class="card">', unsafe_allow_html=True)
email_text = st.text_area(
    "📝 Masukkan Teks Email:",
    height=200,
    placeholder="Ketik atau paste teks email di sini..."
)
st.markdown('</div>', unsafe_allow_html=True)

# Button
if st.button("🔍 Analisis Email"):
    if email_text.strip() == "":
        st.warning("⚠️ Teks email tidak boleh kosong. Silakan masukkan teks email terlebih dahulu.")
    else:
        with st.spinner("🔄 Menganalisis email..."):
            pred = model.predict([email_text])[0]
            proba = model.predict_proba([email_text])[0][1]
        
        # Hasil prediksi
        # st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown("### 📊 Hasil Analisis")
        
        if pred == 1:
            st.markdown('<div class="result-spam">🔴 SPAM</div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="proba-text">⚠️ Tingkat Kepercayaan: <strong>{:.2%}</strong></div>'.format(proba),
                unsafe_allow_html=True
            )
            st.info("🛡️ Email ini kemungkinan besar adalah spam. Berhati-hatilah dengan tautan atau lampiran.")
        else:
            st.markdown('<div class="result-ham">🟢 HAM (Bukan Spam)</div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="proba-text">✅ Tingkat Kepercayaan: <strong>{:.2%}</strong></div>'.format(1 - proba),
                unsafe_allow_html=True
            )
            st.success("✨ Email ini tampak aman dan bukan spam.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <strong>Spam Email Classifier</strong> | Powered by Machine Learning<br>
        © 2025
    </div>
""", unsafe_allow_html=True)