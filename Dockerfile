# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file *first* to leverage Docker cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code into the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# The command to run your app
CMD ["streamlit", "run", "app.py"]