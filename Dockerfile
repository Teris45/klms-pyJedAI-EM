FROM python:3.9
RUN apt-get update && apt-get install -y \
    curl \
    jq \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh
ENTRYPOINT ["./run.sh"]
#ENTRYPOINT ["ls", "-al"]
