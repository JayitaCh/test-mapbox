# Use the official Python image as a base with ARG for flexibility
ARG VARIANT=3.10
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Optional: Install additional system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Optional: Set up a working directory
WORKDIR /workspace
