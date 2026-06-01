FROM python:3.12.5-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /workspace

# The agent carries out the one-way ANOVA audit with the Python standard library
# only — no third-party packages are baked in. The llm-judge's openai client is a
# test-only dependency installed at grading time by tests/test.sh.
COPY input_artifacts/ /workspace/input_artifacts/

CMD ["/bin/bash"]
