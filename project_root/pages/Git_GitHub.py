import streamlit as st

st.set_page_config(page_title="Git & GitHub Tasks", layout="wide")
st.title("🐙 Git & GitHub — Tasks & Commands")

st.markdown("""
This page contains **practical Git & GitHub workflows** from Siddharth Singh's DevOps project.
All commands are directly from the project PDF, ready for your terminal.
""")

tab1, tab2, tab3 = st.tabs([
    "📂 Create & Push Repo",
    "🌿 Branching & Merge",
    "🔀 Fork, Clone & PR"
])

# ---------------- Tab 1 ---------------- #
with tab1:
    st.header("📂 Create a New Repo & Push to GitHub")

    st.write("**Steps:**")
    st.code("""
# 1. Create project folder
mkdir git_hub
cd git_hub

# 2. Create README.md
echo "# $REPO_NAME" > README.md

# 3. Initialize local repo
git init

# 4. Stage and commit changes
git add .
git commit -m "this is my first commit"

# 5. Link to your remote GitHub repo
REPO_URL=https://github.com/$GITHUB_USERNAME/$REPO_NAME.git
git remote add origin $REPO_URL

# 6. Switch to main branch
git branch -M main

# 7. Push to GitHub
git push -u origin main

echo "Repo pushed successfully: $REPO_URL"
""", language="bash")

# ---------------- Tab 2 ---------------- #
with tab2:
    st.header("🌿 Work with Branches & Merge Without Conflicts")

    st.code("""
# 1. Ensure you're on main branch
git checkout main

# 2. Create & switch to new branch
git checkout -b feature1

# 3. Make changes
echo "This is a feature1 update." >> README.md

# 4. Commit changes
git add README.md
git commit -m "feature1: updated README.md with new feature info"

# 5. Switch back to main
git checkout main

# 6. Merge branch
git merge feature1

# 7. Push updates
git push origin main
""", language="bash")

# ---------------- Tab 3 ---------------- #
with tab3:
    st.header("🔀 Fork, Clone & Contribute to Open Source")

    st.code("""
# 1. Fork repository via GitHub UI

# 2. Clone your fork locally
git clone https://github.com/your-username/repo-name.git
cd repo-name

# 3. Add upstream link to original repo
git remote add upstream https://github.com/original-user/repo-name.git
git remote -v

# 4. Create a feature branch
git checkout -b feature-contribution

# 5. Make changes
echo "My contribution to the project" >> CONTRIBUTIONS.md

# 6. Commit changes
git add .
git commit -m "Add: My contribution to CONTRIBUTIONS.md"

# 7. Push your branch
git push origin feature-contribution

# 8. Create Pull Request from GitHub UI
""", language="bash")

st.markdown("---")
st.info("💡 Tip: Run these commands in a terminal with Git installed. Replace placeholders like $REPO_NAME & $GITHUB_USERNAME.")
