import streamlit as st
import pywhatkit
import psutil
import webbrowser
import urllib.parse
from datetime import datetime, timedelta
from PIL import Image, ImageDraw
from twilio.rest import Client

st.set_page_config(page_title="Automation Panel", layout="wide")
st.title("🟣 Automation Panel")

option = st.selectbox(
    "Choose an action:",
    [
        "Select...",
        "1. Send WhatsApp Message",
        "2. Send Email",
        "3. Read RAM Usage",
        "4. Create Image",
        "5. Send SMS"
    ]
)

# 1. WhatsApp Automation
if option == "1. Send WhatsApp Message":
    number = st.text_input("Enter phone number (with country code):", value="+91XXXXXXXXXX")
    message = st.text_area("Enter your message:")
    delay_sec = st.slider("Delay (in seconds from now):", min_value=30, max_value=300, value=60)

    if st.button("Send WhatsApp Message"):
        future_time = datetime.now() + timedelta(seconds=delay_sec)
        hour, minute = future_time.hour, future_time.minute
        try:
            pywhatkit.sendwhatmsg(number, message, hour, minute)
            st.success(f"✅ Message scheduled to {number} at {hour}:{minute}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# 2. Email Automation (via browser)
elif option == "2. Send Email":
    to = st.text_input("Recipient Email:", "example@gmail.com")
    subject = st.text_input("Subject:")
    body = st.text_area("Message Body:")

    if st.button("Send Email (opens Gmail in browser)"):
        params = urllib.parse.urlencode({
            'to': to,
            'subject': subject,
            'body': body
        })
        url = f"https://mail.google.com/mail/?view=cm&fs=1&{params}"
        webbrowser.open(url)
        st.success("✅ Gmail opened in browser.")

# 3. RAM Info
elif option == "3. Read RAM Usage":
    if st.button("Check RAM Usage"):
        memory = psutil.virtual_memory()
        st.write(f"**Total RAM:** {memory.total / (1024 ** 3):.2f} GB")
        st.write(f"**Used RAM:** {memory.used / (1024 ** 3):.2f} GB")
        st.write(f"**Free RAM:** {memory.free / (1024 ** 3):.2f} GB")
        st.write(f"**RAM Usage:** {memory.percent} %")

# 4. Create Image
elif option == "4. Create Image":
    if st.button("Generate Image"):
        width, height = 300, 300
        image = Image.new("RGB", (width, height), "red")
        draw = ImageDraw.Draw(image)
        center = (width // 2, height // 2)
        radius = 80
        draw.ellipse(
            [
                (center[0] - radius, center[1] - radius),
                (center[0] + radius, center[1] + radius)
            ],
            fill="blue"
        )
        path = "generated_image.png"
        image.save(path)
        st.image(path, caption="Generated Image")
        st.success("✅ Image created successfully.")

# 5. Send SMS using Twilio
elif option == "5. Send SMS":
    twilio_sid = st.text_input("Twilio SID", type="password")
    twilio_token = st.text_input("Twilio Auth Token", type="password")
    twilio_number = st.text_input("Twilio Number", value="+1XXXXXXXXXX")
    recipient = st.text_input("Recipient Number", value="+91XXXXXXXXXX")
    sms_msg = st.text_area("SMS Content:")

    if st.button("Send SMS"):
        try:
            client = Client(twilio_sid, twilio_token)
            message = client.messages.create(
                body=sms_msg,
                from_=twilio_number,
                to=recipient
            )
            st.success(f"✅ SMS sent! Message SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ Error sending SMS: {e}")

# Footer
st.markdown("---")
st.info("🟢 All automations above are based on Siddharth Singh's DevOps panel and can be customized for your client project.")
