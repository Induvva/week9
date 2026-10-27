pipeline {
    agent any
    environment {
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Users\\<your-windows-user>\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t kubedemoapp:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASSWORD%'
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag kubedemoapp:v1 induduvva/week9:kubeimage1"
                bat "docker push induduvva/week9:kubeimage1"
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}