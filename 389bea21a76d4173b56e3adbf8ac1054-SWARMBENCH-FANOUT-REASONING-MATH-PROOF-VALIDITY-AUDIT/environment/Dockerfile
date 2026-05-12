FROM python:3.12.10-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl git     && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /logs/agent /logs/verifier

COPY input_artifacts/ /input_artifacts/
WORKDIR /workspace
