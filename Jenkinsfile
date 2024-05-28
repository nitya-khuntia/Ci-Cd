pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // The ID of the Docker Hub credentials in Jenkins
        PROJECT_ID = 'project-ml-424615'
        IMAGE = "gcr.io/${PROJECT_ID}/insurance_claim_model:${env.BUILD_ID}"
        CLUSTER_NAME = 'my-cluster' // Replace with your GKE cluster name
        CLUSTER_ZONE = 'us-central1' // Replace with your GKE cluster zone
        GOOGLE_APPLICATION_CREDENTIALS = credentials('your-gcloud-credentials-id') // Replace with your Google Cloud credentials ID in Jenkins
        DOCKER_IMAGE = "gcr.io/${PROJECT_ID}/insurance_claim_model:${env.BUILD_ID}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/nitya-khuntia/Ci-Cd'
            }
        }

        stage('Verify Docker Installation') {
            steps {
                script {
                    bat 'docker --version'
                }
            }
        }

        // stage('Verify Docker Hub Access') {
        //     steps {
        //         script {
        //             withDockerRegistry([credentialsId: "${DOCKER_CREDENTIALS_ID}", url: 'https://index.docker.io/v1/']) {
        //                 bat 'docker login -u nityakhuntia -p ******** https://index.docker.io/v1/'
        //             }
        //         }
        //     }
        // }

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

        stage('Push Docker Image to GCR') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'your-gcloud-credentials-id', variable: 'GCLOUD_SERVICE_KEY')]) {
                        sh 'echo $GCLOUD_SERVICE_KEY | gcloud auth activate-service-account --key-file=-'
                        sh 'gcloud auth configure-docker --quiet'
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }


        stage('Deploy to GKE') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'your-gcloud-credentials-id', variable: 'GCLOUD_SERVICE_KEY')]) {
                        bat 'echo %GCLOUD_SERVICE_KEY% | gcloud auth activate-service-account --key-file=-'
                        bat 'gcloud config set project %PROJECT_ID%'
                        bat 'gcloud container clusters get-credentials %CLUSTER_NAME% --zone %CLUSTER_ZONE%'
                    }
                    bat 'kubectl apply -f deployment.yaml'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}