# Use an official Python runtime as a parent image
FROM python:3.9

WORKDIR /app

# Copy the list of dependencies
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the training data
COPY data /app/data

# Copy the model data folder
COPY model /app/model

# Copy the training script
COPY src/train.py /app/src/train.py

# Train the model
RUN python src/train.py

# Copy the API source
COPY src/api.py /app/src/api.py

# FastAPI will run on port 8000
EXPOSE 8000

# Run the FastAPI with uvicorn
CMD ["uvicorn", "src.api:api", "--host", "0.0.0.0", "--port", "8000"]