# Use official Python slim image as base
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project directory content into the container's /app folder
COPY . .

# Expose port 8501 for Streamlit web interface
EXPOSE 8501

# Use Streamlit to run the main app (Home.py). 
# "--server.port" to specify 8501 (default)
# "--server.address" 0.0.0.0 binds to all network interfaces
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
