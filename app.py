
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Web Application",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .hero {
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: black;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 36px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 16px;
        margin-bottom: 0;
    }

    .info-card {
        padding: 18px;
        border-radius: 12px;
        background-color: black;
        text-align: center;
        border: 1px solid #dbeafe;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="hero">
    <h1>🤖 AI-Enabled Web Application</h1>
    <p>Smart technology, simple experience.</p>
    <p>Welcome to your interactive AI web platform!</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.subheader("👋 Welcome!")
st.write(
    "Explore this interactive web application built using Python "
    "and Streamlit. Enter your details below to get started."
)

# User input section
st.divider()
st.subheader("📝 User Information")

name = st.text_input(
    "Enter your name",
    placeholder="e.g., Santhosh"
)

email = st.text_input(
    "Enter your email (optional)",
    placeholder="example@email.com"
)

# Submit button
if st.button("🚀 Get Started", use_container_width=True):
    if name.strip():
        st.success(f"Welcome, {name.strip()}! 🎉")
        st.balloons()

        st.markdown("### ✅ Application Status")
        st.write("Your application is running successfully.")

        if email.strip():
            st.info(f"Email provided: {email.strip()}")

        st.caption("Thank you for visiting our AI-enabled platform!")
    else:
        st.warning("Please enter your name before continuing.")

# Feature cards
st.divider()
st.subheader("✨ Application Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🧠 AI Ready</h3>
        <p>Designed for intelligent applications.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>⚡ Fast</h3>
        <p>Simple and responsive interface.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>☁️ Cloud</h3>
        <p>Ready for cloud deployment.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.caption("© 2026 AI-Enabled Web Application | Built with Python & Streamlit")
