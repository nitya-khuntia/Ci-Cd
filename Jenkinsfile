pipeline {
    agent any

    environment {
        PROJECT_ID = 'project-ml-424615'
        IMAGE = "gcr.io/${PROJECT_ID}/insurance_claim_model:${env.BUILD_ID}"
        CLUSTER_NAME = 'my-cluster' // Replace with your GKE cluster name
        CLUSTER_ZONE = 'us-central1' // Replace with your GKE cluster zone
        GOOGLE_APPLICATION_CREDENTIALS = credentials('your-gcloud-credentials-id') // Replace with your Google Cloud credentials ID in Jenkins
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
                    docker.build("${IMAGE}")
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
                    docker.withRegistry('https://gcr.io', GOOGLE_APPLICATION_CREDENTIALS) {
                        docker.image("${IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy to GKE') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'your-gcloud-credentials-id', variable: 'GCLOUD_SERVICE_KEY')]) {
                        sh 'echo $GCLOUD_SERVICE_KEY | gcloud auth activate-service-account --key-file=-'
                        sh 'gcloud config set project ${PROJECT_ID}'
                        sh 'gcloud container clusters get-credentials my-cluster --zone us-central1'
                    }
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }
    }

    post {
        always {
            node {
                cleanWs()
            }
        }
    }
}
