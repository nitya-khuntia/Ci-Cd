pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // The ID of the Docker Hub credentials in Jenkins
        DOCKER_IMAGE = "nityakhuntia/insurance_claim_model:${env.BUILD_ID}" // Ensure this is your Docker Hub username
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nitya-khuntia/Ci-Cd'
            }
        }

        stage('Verify Docker Installation') {
            steps {
                script {
                    bat 'docker --version'
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { return fileExists('Dockerfile') }
            }
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Tests (Optional)') {
            when {
                expression { return fileExists('test_ml_pipeline.py') }
            }
            steps {
                bat 'pytest test_ml_pipeline.py'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python claim.py'
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    def container = docker.image("${DOCKER_IMAGE}")
                    container.run("-d -p 80:80 --name insurance_claim_model_container")
                }
            }
        }
    }
}
