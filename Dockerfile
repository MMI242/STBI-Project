FROM python:3.11-slim

# Install system dependencies
# OpenJDK is required for Pyserini
RUN apt-get update && apt-get install -y \
    default-jdk-headless \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="${JAVA_HOME}/bin:${PATH}"

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Default command
CMD ["flask", "run", "--host=0.0.0.0"]
