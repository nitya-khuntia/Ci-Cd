# Ci-Cd

# Insurance Claim Model CI/CD Pipeline

This project automates the process of training, testing, building, and deploying a machine learning model for insurance claims. The pipeline is implemented using Jenkins, Docker, and Google Kubernetes Engine (GKE).

## Project Overview

- **Train Model**: The model is trained using the `claim.py` script.
- **Run Tests**: Tests are defined in the `test_ml_pipeline.py` script and executed using pytest.
- **Docker Image**: The trained model and necessary environment are containerized using Docker.
- **Google Cloud Platform**: The Docker image is pushed to Google Container Registry (GCR) and deployed to Google Kubernetes Engine (GKE).

## Folder Structure
```plaintext

├── app.py # Flask application for serving the model
├── claim.py # Script to train the insurance claim model
├── deployment.yaml # Kubernetes deployment configuration
├── Dockerfile # Dockerfile to build the Docker image
├── insurance_data_cleaned.csv # Cleaned insurance data for model training
├── Jenkinsfile # Jenkins pipeline script
├── requirements.txt # Python dependencies
├── service.yaml # Kubernetes service configuration
├── test_ml_pipeline.py # Test script for the model
└── README.md # Project documentation
```

## Prerequisites

- **Jenkins**: Ensure you have Jenkins installed and configured with the necessary plugins (e.g., Docker, Google Cloud SDK).
- **Docker**: Docker should be installed and running on the Jenkins server.
- **Google Cloud SDK**: Install the Google Cloud SDK and authenticate with your Google Cloud project.
- **Kubernetes Cluster**: Create a Google Kubernetes Engine (GKE) cluster.

## Jenkins Pipeline Overview

The Jenkins pipeline defined in `Jenkinsfile` includes the following stages:

1. **Checkout Code**: Clone the project repository from GitHub.
2. **Verify Docker Installation**: Check if Docker is installed.
3. **Verify Docker Hub Access**: Log in to Docker Hub.
4. **Build Docker Image**: Build the Docker image from the Dockerfile.
5. **Run Tests (Optional)**: Run tests using pytest.
6. **Train Model**: Train the insurance claim model using `claim.py`.
7. **Push Docker Image to GCR**: Push the Docker image to Google Container Registry (GCR).
8. **Deploy to GKE**: Deploy the Docker image to Google Kubernetes Engine (GKE).

## How to Run

1. **Setup Jenkins Credentials**:
   - **Docker Hub Credentials**: Add your Docker Hub credentials in Jenkins (`docker-hub-credentials`).
   - **Google Cloud Service Account Key**: Add your Google Cloud service account key as a secret file in Jenkins (`gcloud-service-account-key`).

2. **Run the Jenkins Pipeline**:
   - Trigger the Jenkins pipeline manually or set it up to run on code changes.
