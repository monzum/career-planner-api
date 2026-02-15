#!/bin/bash

# ============================================================
# Docker Utility Script - Career Planner API
#
# This script simplifies Docker operations for development.
#
# Supported Commands:
#   build   - Build the Docker image
#   run     - Run container (optional custom port)
#   logs    - Stream container logs
#   stop    - Stop running container
#   status  - Show container status
#
# Works on:
#   macOS, Linux, Windows (Git Bash / WSL)
#
# ============================================================


# -------------------------------
# Configuration Variables
# -------------------------------

# Name of the Docker image
IMAGE_NAME="career-planner-api"

# Name of the running container
CONTAINER_NAME="career-planner-container"

# Default application port
DEFAULT_PORT=8000


# -------------------------------
# CLI Arguments
# -------------------------------

# First argument: action (build/run/logs/etc.)
ACTION=$1

# Second argument: optional port
# If not provided, fallback to DEFAULT_PORT
PORT=${2:-$DEFAULT_PORT}


# -------------------------------
# Function: Display Usage Info
# -------------------------------
usage() {
  echo ""
  echo "Docker Utility Script - Career Planner API"
  echo "-------------------------------------------"
  echo "Usage:"
  echo "  ./docker.sh build            # Build Docker image"
  echo "  ./docker.sh run              # Run container (default port 8000)"
  echo "  ./docker.sh run 9000         # Run container on custom port"
  echo "  ./docker.sh logs             # Stream container logs"
  echo "  ./docker.sh stop             # Stop running container"
  echo "  ./docker.sh status           # Show container status"
  echo ""
}


# -------------------------------
# Function: Build Docker Image
# -------------------------------
build() {
  echo "Building Docker image: $IMAGE_NAME"

  # Build image using Dockerfile in current directory
  docker build -t $IMAGE_NAME .
}


# -------------------------------
# Function: Run Docker Container
# -------------------------------
run() {

  echo "Preparing to run container..."

  # Stop existing container (ignore error if not running)
  docker stop $CONTAINER_NAME 2>/dev/null

  # Remove existing container (ignore error if not present)
  docker rm $CONTAINER_NAME 2>/dev/null

  echo "Starting container on port $PORT..."

  # Run container in detached mode (-d)
  # --env-file loads environment variables from .env file
  # -e PORT overrides the default PORT environment variable
  # -p maps host port to container port
  docker run -d \
    --name $CONTAINER_NAME \
    --env-file .env \
    -p $PORT:$PORT \
    -e PORT=$PORT \
    $IMAGE_NAME

  echo "Container running at: http://localhost:$PORT"
}


# -------------------------------
# Function: View Container Logs
# -------------------------------
logs() {

  echo "Streaming logs for container: $CONTAINER_NAME"

  # -f flag streams logs live
  docker logs -f $CONTAINER_NAME
}


# -------------------------------
# Function: Stop Container
# -------------------------------
stop() {

  echo "Stopping container: $CONTAINER_NAME"

  docker stop $CONTAINER_NAME
}


# -------------------------------
# Function: Check Container Status
# -------------------------------
status() {

  echo "Container status for: $CONTAINER_NAME"

  # Filter running containers by name
  docker ps -f name=$CONTAINER_NAME
}


# -------------------------------
# Command Router
# Determines which function to execute
# -------------------------------
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

  status)
    status
    ;;

  "")
    echo "Error: No command provided."
    usage
    ;;

  *)
    echo "Error: Unknown command '$ACTION'"
    usage
    ;;
esac
