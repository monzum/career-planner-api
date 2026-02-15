#!/bin/bash

# -------------------------------------------
# Docker utility script for Career Planner API
#
# This script allows you to:
# - Build the Docker image
# - Run the container (with optional custom port)
# - View logs
# - Stop the running container
#
# Works on:
# - macOS
# - Linux
# - Windows (Git Bash / WSL)
# -------------------------------------------

# Name of the Docker image
IMAGE_NAME="career-planner-api"

# Name of the container instance
CONTAINER_NAME="career-planner-container"

# Default port if none is provided
DEFAULT_PORT=8000

# First CLI argument (build/run/logs/stop)
ACTION=$1

# Second CLI argument (optional port number)
# If not provided, fallback to DEFAULT_PORT
PORT=${2:-$DEFAULT_PORT}

# -------------------------------------------
# Function: Build Docker Image
# -------------------------------------------
build() {
  echo "Building Docker image: $IMAGE_NAME"
  docker build -t $IMAGE_NAME .
}

# -------------------------------------------
# Function: Run Docker Container
# -------------------------------------------
run() {
  echo "Stopping existing container (if running)..."

  # Stop container if already running (ignore errors)
  docker stop $CONTAINER_NAME 2>/dev/null

  # Remove container if it exists (ignore errors)
  docker rm $CONTAINER_NAME 2>/dev/null

  echo "Starting container on port $PORT..."

  # Run container in detached mode (-d)
  # Map host port to container port
  # Pass PORT environment variable to container
  docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:$PORT \
    -e PORT=$PORT \
    $IMAGE_NAME

  echo "Container running at: http://localhost:$PORT"
}

# -------------------------------------------
# Function: View Container Logs (Live Stream)
# -------------------------------------------
logs() {
  echo "Streaming logs for $CONTAINER_NAME..."
  docker logs -f $CONTAINER_NAME
}

# -------------------------------------------
# Function: Stop Running Container
# -------------------------------------------
stop() {
  echo "Stopping container: $CONTAINER_NAME"
  docker stop $CONTAINER_NAME
}

# -------------------------------------------
# Function: Print Usage Instructions
# -------------------------------------------
usage() {
  echo ""
  echo "Docker Utility Script - Career Planner API"
  echo "-------------------------------------------"
  echo "Usage:"
  echo "  ./docker.sh build           # Build Docker image"
  echo "  ./docker.sh run             # Run container on default port (8000)"
  echo "  ./docker.sh run 9000        # Run container on custom port"
  echo "  ./docker.sh logs            # Stream container logs"
  echo "  ./docker.sh stop            # Stop running container"
  echo ""
}

# -------------------------------------------
# Command Router
# Determines which function to execute
# based on the first CLI argument.
# -------------------------------------------
case "$ACTION" in
  build)
    build
    ;;

  run)
    run
    ;;

  logs)
    logs
    ;;

  stop)
    stop
    ;;

  "" )
    # No command provided
    echo "Error: No command specified."
    usage
    ;;

  * )
    # Invalid command provided
    echo "Error: Unknown command '$ACTION'"
    usage
    ;;
esac
