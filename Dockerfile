# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir mcp>=1.0.0 docker>=7.0.0

# Copy source code
COPY server.py .
COPY src/ ./src/

# Set Python path
ENV PYTHONUNBUFFERED=1

# Expose stdio transport (no port needed for stdio)
# The MCP server communicates via stdin/stdout

# Run the MCP server
ENTRYPOINT ["python", "server.py"]
