FROM python:3.12.5-slim

WORKDIR /workspace

# The agent carries out the one-way ANOVA audit with the Python standard library
# only — no third-party packages are required, and the executable verifier
# (tests/judge.py) is likewise stdlib-only. Nothing test-side is baked in here.

COPY input_artifacts/ /workspace/input_artifacts/

CMD ["bash"]
