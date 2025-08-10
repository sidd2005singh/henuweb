import streamlit as st
import pywhatkit
import psutil
import webbrowser
import urllib.parse
from datetime import datetime, timedelta
from PIL import Image, ImageDraw
from twilio.rest import Client
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

st.set_page_config(page_title="Python Automations", layout="wide")
st.title("🤖 Python Automations")

option = st.selectbox(
    "Choose an action:",
    [
        "Select...",
        "1. Send WhatsApp Message",
        "2. Send Email",
        "3. Read RAM Usage",
        "4. Create Image",
        "5. Send SMS",
        "6. Make Phone Call",
        "7. Google Search",
        "8. Download Web Data",
        "9. LinkedIn Automation (Selenium)",
        "10. Instagram Post"
    ]
)

# WhatsApp
if option == "1. Send WhatsApp Message":
    number = st.text_input("Phone with country code:", value="+91XXXXXXXXXX")
    msg = st.text_area("Message")
    delay_sec = st.slider("Send after seconds:", 30, 300, 60)
    if st.button("Send WhatsApp"):
        ft = datetime.now() + timedelta(seconds=delay_sec)
        try:
            pywhatkit.sendwhatmsg(number, msg, ft.hour, ft.minute)
            st.success("✅ WhatsApp scheduled")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Email via Gmail Compose
elif option == "2. Send Email":
    to = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    if st.button("Open Gmail"):
        params = urllib.parse.urlencode({'to': to, 'subject': subject, 'body': body})
        webbrowser.open(f"https://mail.google.com/mail/?view=cm&fs=1&{params}")
        st.success("✅ Gmail compose opened in browser")

# RAM Usage
elif option == "3. Read RAM Usage":
    if st.button("Check RAM"):
        mem = psutil.virtual_memory()
        st.json({
            "Total GB": mem.total / (1024 ** 3),
            "Used GB": mem.used / (1024 ** 3),
            "Free GB": mem.free / (1024 ** 3),
            "Percent": mem.percent
        })

# Create Image
elif option == "4. Create Image":
    if st.button("Generate Image"):
        image = Image.new("RGB", (300, 300), "red")
        draw = ImageDraw.Draw(image)
        draw.ellipse((110, 110, 190, 190), fill="blue")
        image.save("generated_image.png")
        st.image("generated_image.png", caption="Generated Image")
        st.success("✅ Image saved and displayed")

# Send SMS
elif option == "5. Send SMS":
    sid = st.text_input("Twilio SID", type="password")
    token = st.text_input("Twilio Auth Token", type="password")
    from_no = st.text_input("Twilio From Number", "+1XXXXXXXXXX")
    to_no = st.text_input("To Number", "+91XXXXXXXXXX")
    sms_msg = st.text_area("Message")
    if st.button("Send SMS"):
        try:
            client = Client(sid, token)
            m = client.messages.create(body=sms_msg, from_=from_no, to=to_no)
            st.success(f"✅ SMS sent, SID: {m.sid}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Make Phone Call
elif option == "6. Make Phone Call":
    sid = st.text_input("Twilio SID", type="password")
    token = st.text_input("Twilio Token", type="password")
    from_no = st.text_input("Twilio From Number")
    to_no = st.text_input("Recipient Number")
    twiml_url = st.text_input("Twiml URL", value="http://demo.twilio.com/docs/voice.xml")
    if st.button("Call"):
        try:
            client = Client(sid, token)
            call = client.calls.create(to=to_no, from_=from_no, url=twiml_url)
            st.success(f"✅ Call initiated, SID: {call.sid}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Google Search
elif option == "7. Google Search":
    query = st.text_input("Search term")
    if st.button("Search"):
        try:
            from googlesearch import search
            results = list(search(query, num_results=5))
            for link in results:
                st.markdown(f"[{link}]({link})")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Download Web Data
elif option == "8. Download Web Data":
    url = st.text_input("URL", "https://en.wikipedia.org/wiki/Python_(programming_language)")
    d_type = st.radio("What to download?", ["Tables", "Images"])
    if st.button("Download"):
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            resp = requests.get(url, headers=headers)
            if d_type == "Tables":
                tables = pd.read_html(resp.text)
                for i, table in enumerate(tables, 1):
                    st.write(f"Table {i}")
                    st.dataframe(table)
            else:
                soup = BeautifulSoup(resp.text, "html.parser")
                for img in soup.find_all("img"):
                    src = img.get("src")
                    if src:
                        src = src if src.startswith("http") else "https:" + src
                        st.image(src)
        except Exception as e:
            st.error(f"❌ Error: {e}")

# LinkedIn Automation - Selenium Placeholder
elif option == "9. LinkedIn Automation (Selenium)":
    st.warning("ℹ Selenium automation not runnable in Streamlit Cloud directly.\nRun locally in Python to automate LinkedIn.")

# Instagram Automation - Instagrapi Placeholder
elif option == "10. Instagram Post":
    st.warning("ℹ Instagram automation requires instagrapi session & local environment.")
