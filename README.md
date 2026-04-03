
# Career Decision Platform

Backend service for **tracking job applications, comparing offers, and analyzing career decisions**.

The project explores **modern backend engineering practices**, including containerized development workflows and cloud deployment using AWS.

---

## Tech Stack

**Backend**
- Python
- FastAPI
- Pydantic
- REST APIs

**Infrastructure**
- Docker
- Bash automation scripts
- Container health checks

**Cloud (planned)**
- AWS ECS
- AWS ECR
- PostgreSQL

---

## Features

- Job application tracking API
- Versioned REST endpoints
- Request validation using Pydantic
- Structured logging middleware
- Dockerized backend service
- Automated Docker build/run workflow
- Container health monitoring

---

## Architecture

Client / Frontend (future)
        |
        v
     FastAPI API
        |
        v
   Docker Container
        |
        v
      AWS ECS
        |
        v
   PostgreSQL Database

---

## Running Locally

Build the Docker image:

```bash
./docker.sh build
```

Run the container:

```bash
./docker.sh run
```

Default server:

http://localhost:8000

Run on a different port:

```bash
./docker.sh run 9000
```

---

## API Documentation

FastAPI automatically generates interactive documentation.

After starting the server:

http://localhost:8000/docs

---

## Example API Request

Create a job application entry:

POST /api/v1/applications

Example request body:

```json
{
  "company": "Example Corp",
  "position": "Software Engineer",
  "location": "Toronto",
  "status": "applied"
}
```

---

## Future Improvements

Planned features include:

- AWS deployment using ECS
- PostgreSQL database integration
- Job listing aggregation from multiple sources
- Resume and cover letter generation
- Offer comparison and cost-of-living analysis
- Interview preparation resources

---

## Author

Monzur Murshed Muhammad

GitHub: https://github.com/monzum
