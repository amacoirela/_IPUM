# Dockerfile

# Use a minimal Python image as the base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

# Copy only dependency files first (to leverage caching)
COPY pyproject.toml uv.lock ./

# Verify uv installation
RUN uv --version

# Install project dependencies using uv
RUN uv pip sync --system uv.lock

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]