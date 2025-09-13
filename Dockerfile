FROM python:3.11-slim

WORKDIR /app

COPY src/ ./src/

ENTRYPOINT ["python", "src/calculator.py"]
# Default args (can be overridden at docker run)
CMD ["--mode", "service"]
