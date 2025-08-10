import streamlit as st

st.set_page_config(page_title="🐳 Docker Tasks", layout="wide")
st.title("🐳 Docker - Case Studies & Hands-On Experiments")

st.markdown("""
## 📌 Why Use Docker on RHEL 9?
- Container-ready, enterprise grade platform.
- Isolates applications & their dependencies.
- Works perfectly with cloud & DevOps pipelines.
---
""")

# Case studies section
st.header("🏢 Real-World Docker Case Studies")
case = st.selectbox("Select a case study", [
    "Spotify — Microservices at Scale",
    "ADP — Consistent Dev Environments",
    "Walmart Labs — Faster CI/CD",
    "ML Startups — Portability & GPU Support"
])

if case == "Spotify — Microservices at Scale":
    st.write("""
**Challenge:** Complex microservices deployments.  
**Solution:** Dockerized services + Kubernetes orchestration.  
**Result:** 94% faster deployments, simpler scaling.
""")
elif case == "ADP — Consistent Dev Environments":
    st.write("""
**Challenge:** Environment inconsistencies across team members.  
**Solution:** Docker images with RHEL 9 base.  
**Result:** Identical, reproducible environments.
""")
elif case == "Walmart Labs — Faster CI/CD":
    st.write("""
**Challenge:** CI/CD bottlenecks due to lengthy environment setup.  
**Solution:** Pre-built Docker images for test stages.  
**Result:** Cut CI times by 70%.
""")
elif case == "ML Startups — Portability & GPU Support":
    st.write("""
**Challenge:** Ship ML models with full dependencies.  
**Solution:** NVIDIA-Docker for GPU containers.  
**Result:** One-click deploy anywhere with GPUs.
""")

st.divider()

# Experiments Section
st.header("🧪 Docker Hands-On from Project PDF")
exp = st.selectbox("Choose Experiment", [
    "1. Run Python in Docker",
    "2. Run Apache in Docker",
    "3. Run Flask App in Docker",
    "4. Docker Inside Docker (DinD)",
    "5. Firefox Browser in Docker (GUI)",
    "6. Play VLC in Docker",
    "7. Apache on RHEL 9 UBI",
    "8. Menu-based CLI App in Docker",
    "9. Linear Regression in Docker"
])

if exp == "1. Run Python in Docker":
    st.code("""
docker pull python:3.12-slim
echo 'print("Hello from Docker!")' > hello.py
docker run --rm -v "$PWD":/usr/src/app -w /usr/src/app python:3.12-slim python hello.py
""", language="bash")

elif exp == "2. Run Apache in Docker":
    st.code("""
docker pull httpd:2.4
mkdir apache-site
echo "<h1>Hello from Apache in Docker</h1>" > apache-site/index.html
docker run -dit --name my-apache -p 8080:80 -v "$PWD/apache-site":/usr/local/apache2/htdocs/ httpd:2.4
""", language="bash")

elif exp == "3. Run Flask App in Docker":
    st.code("""
# app.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Flask in Docker!"
if __name__ == '__main__':
    app.run(host='0.0.0.0')

# Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]

# Build & Run
docker build -t flask-app .
docker run -p 5000:5000 flask-app
""", language="bash")

elif exp == "4. Docker Inside Docker (DinD)":
    st.code("""
docker run --privileged --name dind-test -d docker:dind
docker exec -it dind-test sh
docker run hello-world
""", language="bash")

elif exp == "5. Firefox Browser in Docker (GUI)":
    st.code("""
# Dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y firefox x11-apps && apt-get clean
# Build & run with X11 access
docker build -t firefox-container .
xhost +local:root
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  firefox-container firefox
""", language="bash")

elif exp == "6. Play VLC in Docker":
    st.code("""
# Dockerfile
FROM registry.access.redhat.com/ubi9/ubi
RUN dnf install -y vlc xorg-x11-server-utils libX11 libXext alsa-lib && dnf clean all
CMD ["vlc"]

docker build -t vlc-rhel9 .
xhost +local:root
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$PWD:/media" \
  vlc-rhel9
""", language="bash")

elif exp == "7. Apache on RHEL 9 UBI":
    st.code("""
# Dockerfile
FROM registry.access.redhat.com/ubi9/ubi
RUN dnf install -y httpd && dnf clean all
COPY index.html /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]

# Build & run
docker build -t rhel9-apache .
docker run -dit -p 8080:80 rhel9-apache
""", language="bash")

elif exp == "8. Menu-based CLI App in Docker":
    st.code("""
# app.py
def menu():
    while True:
        print("\\n1. Greet\\n2. Add Numbers\\n3. Exit")
        ch = input("Choice: ")
        if ch == "1":
            print("Hello!")
        elif ch == "2":
            a = int(input("First: ")); b=int(input("Second: "))
            print(f"Sum={a+b}")
        elif ch == "3": break
        else: print("Invalid")

if __name__ == "__main__":
    menu()

# Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]

# Build & Run
docker build -t menu-cli-app .
docker run -it menu-cli-app
""", language="bash")

elif exp == "9. Linear Regression in Docker":
    st.code("""
# lr.py
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1],[2],[3],[4]])
y = np.array([1,2,3,4])
model = LinearRegression().fit(X,y)
print("Coefficient:", model.coef_[0])

# Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY lr.py .
RUN pip install scikit-learn numpy
CMD ["python", "lr.py"]

docker build -t lr-app .
docker run lr-app
""", language="bash")

st.divider()
st.info("💡 All commands above are taken directly from the project PDF — copy & run in terminal with Docker installed.")
