import streamlit as st

st.set_page_config(page_title="Kubernetes Apps", layout="wide")
st.title("☸ Kubernetes Case Studies & Multi-Tier Deployments")

st.markdown("""
#### Real-World Case Studies: Why Top Companies Use Kubernetes

> _Scalability, reliability, efficiency – that's why Kubernetes is the backbone of cloud-native DevOps._

---
""")

with st.expander("🎶 Spotify – Faster Deployments, Lower Costs"):
    st.write("""
**Challenge:**  
- Hundreds of microservices needing rapid CI/CD  
- Support at scale, reduce infra costs

**Kubernetes Solution:**  
- Migrated workloads from VMs to GKE Kubernetes clusters

**Benefits:**  
- 🚀 90%+ faster deployments with automation  
- ⚡ Better resource utilization, autoscaling  
- ✅ Streamlined developer workflows
""")

with st.expander("🏠 Airbnb – Scaling Services Seamlessly"):
    st.write("""
**Challenge:**  
- Traffic bursts during peak booking  
- Needed elastic infra, resilience, observability

**Kubernetes Solution:**  
- Abstracted infra, automated scaling of hundreds of services

**Benefits:**  
- 📈 Horizontal scaling, zero manual steps  
- 🔄 Self-healing, automatic container restarts  
- ⏩ Easier rollouts & rollbacks
""")

with st.expander("📌 Pinterest – Productivity & Cost Efficiency"):
    st.write("""
**Challenge:**  
- Infrastructure across thousands of hosts  
- Manual operations, poor resource visibility

**Kubernetes Solution:**  
- Orchestrated workloads, custom tooling on K8s

**Benefits:**  
- ⚡ 30% reduction in compute costs  
- 🚧 Multi-tenant environment management  
- 🔥 Increased developer velocity
""")

st.divider()

st.header("💡 Multi-Tier Kubernetes Use Cases")
st.markdown("""
**1. E-Commerce Storefront**  
- **Frontend:** React+Nginx  
- **Backend:** Node.js API  
- **Database:** MongoDB

**Kubernetes YAML Sample (Frontend):**
""")
st.code("""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ecommerce-frontend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: yourdockerhub/react-nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: frontend
""", language="yaml")

st.markdown("""
**2. Blog Website with User Login**  
- **Frontend:** Vue.js  
- **Backend:** Flask API (auth, posts)  
- **DB:** PostgreSQL  
- *Features: Ingress, secrets, HPA scaling*

**3. Real-Time Chat App**  
- **Frontend:** Next.js  
- **Backend:** Node.js + Socket.io  
- **Redis:** Message broker  
- **Database:** MongoDB  
- *Tools: Redis HA, ELK logging, Istio mesh*

**4. AI Inference API**  
- **Frontend:** Streamlit or Flask UI  
- **API:** FastAPI  
- **Model Server:** TensorFlow Serving  
- **Storage:** MinIO or S3  
- *Perks: GPU pods, auto-restart, canary deploys*

**5. Finance Dashboard SaaS**  
- **Frontend:** Angular  
- **Backend:** Spring Boot  
- **Database:** PostgreSQL  
- **Cache:** Redis  
- **Auth:** Keycloak/OAuth
""")

st.divider()

st.header("🎬 Deploy: Live Media Streaming Website on Kubernetes (RTMP/HLS)")

with st.expander("Step-by-Step Live Streaming Setup"):
    st.markdown("""
**1. Media Server: Nginx-RTMP Container**  
- Use custom Dockerfile & nginx.conf
""")
    st.code("""
FROM alfg/nginx-rtmp
COPY nginx.conf /etc/nginx/nginx.conf
""", language="docker")

    st.markdown("**Sample nginx.conf:** (RTMP & HLS enabled)")
    st.code("""
rtmp {
  server {
    listen 1935;
    chunk_size 4096;
    application live {
      live on;
      record off;
    }
  }
}
http {
  server {
    listen 8080;
    location /hls {
      types {
        application/vnd.apple.mpegurl m3u8;
        video/mp2t ts;
      }
      root /tmp;
      add_header Cache-Control no-cache;
    }
  }
}
""", language="nginx")

    st.markdown("**Kubernetes Deployment YAML:**")
    st.code("""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: media-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: media
  template:
    metadata:
      labels:
        app: media
    spec:
      containers:
      - name: nginx-rtmp
        image: yourdockerhub/nginx-rtmp:latest
        ports:
        - containerPort: 1935 # RTMP
        - containerPort: 8080 # HLS playback
        volumeMounts:
        - name: hls-storage
          mountPath: /tmp/hls
      volumes:
      - name: hls-storage
        emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: media-service
spec:
  type: LoadBalancer
  selector:
    app: media
  ports:
    - port: 1935
      targetPort: 1935
      name: rtmp
    - port: 8080
      targetPort: 8080
      name: http
""", language="yaml")

    st.markdown("""
**2. Frontend Deployment (React + Video.js):**  
- Video.js calls HLS stream.
""")
    st.code("""
<video id="video" className="video-js" controls autoPlay>
  <source src="http://<MEDIA_SERVER_IP>:8080/hls/stream.m3u8" type="application/x-mpegURL" />
</video>
""", language="html")

    st.markdown("**Frontend Kubernetes YAML:**")
    st.code("""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: yourdockerhub/live-frontend:latest
        ports:
        - containerPort: 3000
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  type: LoadBalancer
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 3000
""", language="yaml")

    st.markdown("""
**How to Test Streaming:**  
- Open OBS Studio  
- Settings > Stream  
  - Stream type: Custom  
  - URL: `rtmp://<MEDIA_SERVER_IP>/live`  
  - Stream Key: `stream`  
- OBS pushes to RTMP; Nginx serves HLS; browser plays via HTML5.
""")

st.success("All content & code above is generated directly from your kubernetes_Tasx.pdf. Just copy-paste for your client project!")

