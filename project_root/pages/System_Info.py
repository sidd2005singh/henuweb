import streamlit as st
import psutil
import platform

st.title("🖥️ System Info & Resource Monitoring")

if st.button("Show RAM Usage"):
    mem = psutil.virtual_memory()
    st.json({
        "Total GB": mem.total / (1024 ** 3),
        "Used GB": mem.used / (1024 ** 3),
        "Free GB": mem.free / (1024 ** 3),
        "Percent": mem.percent
    })

if st.button("Show CPU Usage"):
    st.write(f"CPU Usage: {psutil.cpu_percent()} %")

if st.button("Show Disk Usage"):
    # Use raw string or double backslash for Windows paths
    if platform.system() == "Windows":
        disk = psutil.disk_usage(r'C:\\')  # Raw string to avoid escape errors
    else:
        disk = psutil.disk_usage('/')
    st.json({
        "Total GB": disk.total / (1024 ** 3),
        "Used GB": disk.used / (1024 ** 3),
        "Free GB": disk.free / (1024 ** 3),
        "Percent": disk.percent
    })
