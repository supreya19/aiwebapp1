import streamlit as st

import google.generativeai as genai
genai.configure(api_key="AIzaSyCKWuEoRpCP9TJAttoxj0TMZwHXNu0tYfQ")
model = genai.GenerativeModel("gemini-2.0-flash")

st.title("แปลภาษา")
ch = st.selectbox("เลือกภาษาปลายทาง",
                 ("ไทย","อังกฤษ","เกาหลี","ญี่ปุ่น"))

text_in = st.text_input("ป้อนข้อความที่ต้องการแปล: ")

prompt = "แปลข้อความต่อไปนี้เป็นภาษา"+ ch + " " + text_in + " โดยไม่ต้องมีคำอธิบาย"
st.text(prompt)

if st.button("แปล"):
    try:
        response = model.generate_content(prompt)
        st.text(response.text)
    except:
        st.text("no response")




    



