pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-hello-world .'
            }
        }

        stage('Run App Container') {
            steps {
                sh 'docker run -d --rm -p 5000:5000 --name flask_app flask-hello-world'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                pip install pytest playwright
                playwright install --with-deps
                pytest tests/test_app.py -q
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker stop flask_app || true'
            }
        }
    }
}
