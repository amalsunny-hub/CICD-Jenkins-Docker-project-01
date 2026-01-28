pipeline {
    agent any

    environment {
        IMAGE_NAME = 'amalsunny27/my-app'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                bat '''
                docker build -t %IMAGE_NAME%:%IMAGE_TAG% .
                '''
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    bat '''
                    echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin
                    docker push %IMAGE_NAME%:%IMAGE_TAG%
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                echo ===== DEPLOY START =====
                docker stop cicd-container || echo No container to stop
                docker rm cicd-container || echo No container to remove

                docker run -d -p 5000:5000 --name cicd-container %IMAGE_NAME%:%IMAGE_TAG%

                echo ===== RUNNING CONTAINERS =====
                docker ps
                '''
            }
        }
    }
}
