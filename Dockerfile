# FROM python:3.10

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .

# ENTRYPOINT ["python", "main.py"]

FROM python:3.10

WORKDIR /app

COPY main.py .

ENTRYPOINT ["python", "main.py"]

