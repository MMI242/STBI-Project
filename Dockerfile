FROM python:3.11-slim

# Install system dependencies
# OpenJDK is required for Pyserini
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

WORKDIR /app

# Install Python packages mentioned in README
RUN pip install --no-cache-dir \
    flask \
    pyserini \
    scispacy \
    spacy

# Install scispaCy model (en_core_sci_sm)
# This URL is for scispacy v0.5.4 which is compatible with spacy>=3.7
RUN pip install --no-cache-dir https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz

# Copy the rest of the application
COPY . .

# Expose the Flask port
EXPOSE 5000

# Default command
CMD ["flask", "run", "--host=0.0.0.0"]
