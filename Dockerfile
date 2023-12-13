FROM python:3.8-slim
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "run.py"]
