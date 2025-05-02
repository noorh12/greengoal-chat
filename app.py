
import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="GreenGoal Chatbot", page_icon=":soccer:", layout="centered")

# تحميل الصورة
logo = Image.open("greengoal_logo_avatar_circular.png")
st.image(logo, width=100)

# عنوان ترحيبي
st.markdown("<h1 style='text-align: center; color: green;'>GreenGoal Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Welcome! Choose your language and ask me anything about GreenGoal!</p>", unsafe_allow_html=True)

# اختيار اللغة
language = st.radio("Select Language / اختر اللغة", ("English", "العربية"))

# حقل إدخال المستخدم
user_input = st.text_input("Type your message below / اكتب رسالتك بالأسفل:")

# تحميل نماذج التنبؤ
attendance_model = joblib.load("attendance_predictor_model.pkl")
weather_model = joblib.load("weather_predictor_model.pkl")
winner_model = joblib.load("logreg_winner_predictor_model.pkl")

# تحميل المحولات
le_country = joblib.load("le_country.pkl")
le_group = joblib.load("le_group_att.pkl")
le_weather = joblib.load("le_weather_att.pkl")
le_season = joblib.load("le_season_att.pkl")

# الرد على المستخدم
def generate_response(msg):
    msg_lower = msg.lower()

    if language == "English":
        if "winner" in msg_lower:
            return "The predicted winner based on previous data is: Argentina"
        elif "weather" in msg_lower:
            return "The predicted weather is: Sunny"
        elif "attendance" in msg_lower or "people" in msg_lower:
            return "Expected number of attendees: 56,000"
        elif "places" in msg_lower or "tourism" in msg_lower:
            return "Please select a city to view tourist attractions: [Jeddah, Riyadh, Abha, AlUla, Dammam, Khobar, Ahsa]"
        else:
            return "Sorry, I didn’t understand. Try asking about the winner, weather, or tourist places."
    else:
        if "الفائز" in msg_lower:
            return "الفريق المتوقع فوزه بناءً على البيانات هو: الأرجنتين"
        elif "الطقس" in msg_lower:
            return "الطقس المتوقع: مشمس"
        elif "الحضور" in msg_lower or "عدد" in msg_lower:
            return "عدد الحضور المتوقع: 56,000"
        elif "أماكن" in msg_lower or "سياحة" in msg_lower:
            return "الرجاء اختيار مدينة لعرض أماكنها السياحية: [جدة، الرياض، أبها، العلا، الدمام، الخبر، الأحساء]"
        else:
            return "عذرًا، لم أفهم. جرّب تسألني عن الطقس أو الفائز أو الأماكن السياحية."

# عرض الرد
if user_input:
    st.markdown(f"<div style='background-color:#d4edda; padding:10px; border-radius:10px;'><strong>You:</strong> {user_input}</div>", unsafe_allow_html=True)
    response = generate_response(user_input)
    st.markdown(f"<div style='background-color:#f8f9fa; padding:10px; border-radius:10px;'><strong>GreenGoal Bot:</strong> {response}</div>", unsafe_allow_html=True)
