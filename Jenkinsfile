pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/fadykaram88/todo-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t todo-app .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'npm install'
                    sh 'npm test'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 3000:3000 todo-app'
                }
            }
        }
    }

    post {
        success {
            slackSend(channel: '#your-channel', message: "Build succeeded!")
        }
        failure {
            slackSend(channel: '#your-channel', message: "Build failed!")
        }
    }
}
