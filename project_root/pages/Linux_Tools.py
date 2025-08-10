import streamlit as st

st.set_page_config(page_title="Linux Tools", layout="wide")
st.title("🐧 Linux Customization & Automation Tools")

st.header("1️⃣ Change Application Icon in Linux")
st.write("""
**Steps:**
1. Locate `.desktop` file (usually `/usr/share/applications/` or `~/.local/share/applications/`)
2. Copy system-wide file to local if needed.
3. Edit `Icon=` line with custom image path.
4. Run `gtk-update-icon-cache` to refresh.
5. Restart app / log out & log in.
""")
st.code("""
cp /usr/share/applications/nautilus.desktop ~/.local/share/applications/
nano ~/.local/share/applications/nautilus.desktop
Icon=/home/user/Pictures/custom-icon.png
gtk-update-icon-cache
""", language="bash")

st.header("2️⃣ Why Companies Use Linux")
st.markdown("""
- **Open Source Freedom** – No license fees, complete control.
- **Security** – Used in NASA, Google, Netflix.
- **Scalable** – From IoT devices to supercomputers.
- **Cloud-Ready** – Works perfectly with AWS, Kubernetes, Docker.
""")

st.header("3️⃣ GUI Programs & Commands Behind Them")
st.table([
    ["GParted", "parted, mkfs, lsblk, blkid"],
    ["GNOME Software", "apt, dnf, flatpak, pkcon"],
    ["Nautilus", "cp, mv, rm, chmod, gio open"],
    ["System Monitor", "top, ps, free, df, iostat"],
    ["Network Manager", "nmcli, ip, ping, dig"]
])

st.header("4️⃣ Add More Terminals / GUI in Linux")
st.code("""
sudo dnf install tmux i3 i3status dmenu xterm rofi
sudo systemctl reboot
""")

st.header("5️⃣ Communication from Terminal")
st.code("""
# Email
echo "body" | mailx -s "Subject" user@example.com

# WhatsApp via Twilio API
curl -X POST https://api.twilio.com/... \
--data-urlencode "From=whatsapp:+1..." \
--data-urlencode "To=whatsapp:+91..." \
--data-urlencode "Body=Hello from CLI" \
-u ACCOUNT_SID:AUTH_TOKEN

# Tweet via t CLI
t update "Hello from Linux CLI!"

# SMS via Twilio API
curl -X POST https://api.twilio.com/... \
--data-urlencode "To=+91..." \
--data-urlencode "From=+1..." \
--data-urlencode "Body=Hello" \
-u ACCOUNT_SID:AUTH_TOKEN
""", language="bash")

st.header("6️⃣ Ctrl+C & Ctrl+Z Signals")
st.write("""
- **Ctrl+C** → Sends SIGINT (2) to terminate process gracefully.
- **Ctrl+Z** → Sends SIGTSTP (20) to suspend process to background.
""")
