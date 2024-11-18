pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // هنا بنحدد الفرع اللي اسمه 'main'
                git branch: 'main', url: 'https://github.com/fadykaram88/todo-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // بناء Docker image
                    sh 'docker build -t todo-app .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // تثبيت الحزم وتشغيل الاختبارات
                    sh 'npm install'
                    sh 'npm test'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // تشغيل Docker container
                    sh 'docker run -d -p 3000:3000 todo-app'
                }
            }
        }
    }
}
