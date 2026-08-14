# Use a lightweight Python 3.11 image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install all required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit application into the container
COPY app.py .

# Expose Streamlit's default port
EXPOSE 8501

# Start the Streamlit application
# --server.address=0.0.0.0 allows access from outside the container
# --server.port=8501 sets the application port
# --server.headless=true runs Streamlit without opening a browser
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]