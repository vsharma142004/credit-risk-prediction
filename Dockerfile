FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY app.py .
COPY model.pkl .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
