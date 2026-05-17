FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/*

WORKDIR /testbed
COPY input_artifacts/ /testbed/input_artifacts/
RUN mkdir -p /logs/verifier
