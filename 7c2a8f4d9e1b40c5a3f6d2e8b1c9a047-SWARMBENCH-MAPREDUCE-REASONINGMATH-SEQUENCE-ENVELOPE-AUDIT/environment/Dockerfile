FROM python:3.12.7-slim
RUN apt-get update     && apt-get install -y --no-install-recommends curl git ca-certificates     && rm -rf /var/lib/apt/lists/*
COPY input_artifacts/ /input_artifacts/
WORKDIR /workspace
RUN mkdir -p /logs /workspace \
    && ln -s /input_artifacts /workspace/input_artifacts \
    && ln -s /logs /workspace/logs
