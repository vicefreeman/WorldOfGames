pipeline {
    agent any
    environment {
		DOCKERHUB_CREDENTIALS=credentials('docker_hub_login')
	}
    stages {
        stage('Initializing') {
            steps {
                sh 'echo "JENKINS IS RUNNING" '
            }
        }
        stage('Git Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/vicefreeman/WorldOfGames.git']]])
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker compose up -d'
                }
            }
        }
        stage('Run test') {
            steps {
                script {
                    sh 'python3 ./tests/e2e.py '
                }
            }
        }
        stage('Login to HUB') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push Image') {
            steps{
                sh 'docker push vicefreeman/python_flask_wog:python_flask_wog'
            }
        }
    }
}
