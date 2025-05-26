# ---------- Build Stage ----------
FROM maven:3.9.6-eclipse-temurin-11 AS builder

WORKDIR /build

# Copy entire serial module so we ensure a fresh build each time
COPY serial /build/serial

# Build the jar (skip tests, name it jedai.jar)
RUN mvn -f /build/serial/pom.xml clean package


# ---------- Runtime Stage ----------
FROM ubuntu:22.04

# Install Python, Java, and tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        curl \
        jq \
        default-jre-headless \
        ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /build/serial/target/geospatialinterlinking-1.0-SNAPSHOT-jar-with-dependencies.jar ./jedai.jar
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh

# Entry point
ENTRYPOINT ["./run.sh"]