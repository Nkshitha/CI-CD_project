# DevOps CI/CD Project

End-to-end CI/CD pipeline with Jenkins, Docker and Kubernetes.

## Architecture
```
GitHub Push → Jenkins Pipeline → Docker Build → Kubernetes Deploy
```

## Tech Stack

- **App**: Python Flask
- **Container**: Docker (multi-stage build)
- **Orchestration**: Kubernetes (Minikube)
- **CI/CD**: Jenkins
- **IaC**: Terraform (Project 3)
- **Config Management**: Ansible (Project 4)

## Project Structure
```
devops-cicd-project/
├── app/
│   ├── app.py              # Flask application
│   └── requirements.txt    # Python dependencies
├── tests/
│   └── test_app.py         # Unit tests
├── k8s/
│   ├── deployment.yaml     # Kubernetes deployment
│   ├── service.yaml        # Kubernetes service
│   ├── configmap.yaml      # App configuration
│   └── namespace.yaml      # Namespace definition
├── jenkins/
│   └── Jenkinsfile         # CI/CD pipeline
├── Dockerfile              # Multi-stage Docker build
└── README.md
```

## Endpoints

| Endpoint  | Method | Description        |
|-----------|--------|--------------------|
| /         | GET    | Service info       |
| /health   | GET    | Health check       |
| /metrics  | GET    | App metrics        |

## Pipeline Stages

1. **Checkout**   → Pull code from GitHub
2. **Test**       → Run pytest unit tests
3. **Build**      → Build Docker image
4. **Load**       → Load image to Minikube
5. **Deploy**     → Rolling update to Kubernetes
6. **Verify**     → Health check post-deploy

## Running Locally
```bash
# Run tests
python3 -m pytest tests/ -v

# Build Docker image
docker build -t devops-cicd-project:1.0.0 .

# Run container
docker run -p 5000:5000 devops-cicd-project:1.0.0

# Deploy to Kubernetes
kubectl apply -f k8s/
```
