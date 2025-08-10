import streamlit as st

st.set_page_config(page_title="Cloud & DevOps Blogs", layout="wide")
st.title("📝 Case Studies & Technical Blogs by Siddharth Singh")

topic = st.selectbox("Select a Blog", [
    "AWS Case Studies",
    "Amazon S3 Storage Classes",
    "Docker Case Studies",
    "Kubernetes Case Studies",
    "Companies Using Linux"
])

if topic == "AWS Case Studies":
    st.header("🚀 AWS Transforming Businesses")
    st.subheader("Netflix — Scaling Global Streaming")
    st.write("""
- Migrated entirely to AWS: Used EC2, S3, CloudFront, Lambda, DynamoDB.
- Achieved 99.99% uptime, personalized recommendations.
""")
    st.subheader("Moderna — Accelerating Vaccine Development")
    st.write("""
- Used AWS EC2 HPC, S3, AWS Batch for R&D.
- Delivered COVID-19 vaccine candidate in 42 days.
""")

elif topic == "Amazon S3 Storage Classes":
    st.write("""
**S3 Standard** — High availability for frequent access  
**S3 Intelligent-Tiering** — Auto-moves data between tiers  
**S3 Glacier** — Archival with low cost
""")

elif topic == "Docker Case Studies":
    st.write("""
**Spotify:** 94% faster deployments with Docker microservices.  
**ADP:** Unified dev environments with RHEL 9 + Docker.  
**Walmart Labs:** Faster CI/CD feedback loops.
""")

elif topic == "Kubernetes Case Studies":
    st.write("""
**Spotify:** 90%+ faster deployments via GKE.  
**Airbnb:** Auto-scaled infrastructure without downtime.  
**Pinterest:** 30% reduced compute costs.
""")

elif topic == "Companies Using Linux":
    st.write("""
**Google, NASA, Netflix** — because Linux is secure, open, and high-performance.  
Used everywhere from cloud data centers to supercomputers.
""")
