# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
 
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

RUN chmod -R 775 /app

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
# CMD ["python","-m", "streamlit", "run", "src/streamlit_app.py"]

CMD ["./start.sh"]
