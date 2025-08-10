import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

st.title("🌐 Web Data Downloader")

url = st.text_input("Enter a URL (e.g. Wikipedia page)")
task = st.radio("Select Task", ["Download Tables", "Download Images"])

if st.button("Start"):
    headers = {"User-Agent": "Mozilla/5.0"}
    if task == "Download Tables":
        try:
            resp = requests.get(url, headers=headers)
            tables = pd.read_html(resp.text)
            for i, table in enumerate(tables, start=1):
                st.write(f"Table {i}")
                st.dataframe(table)
        except Exception as e:
            st.error(f"No tables found or error: {e}")
    elif task == "Download Images":
        try:
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, "html.parser")
            imgs = []
            for img in soup.find_all("img"):
                src = img.get("src")
                if src:
                    img_url = urljoin(url, src)
                    imgs.append(img_url)
            for img_link in imgs:
                st.image(img_link)
        except Exception as e:
            st.error(f"Error: {e}")
