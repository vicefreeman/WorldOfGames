pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vicefreeman/python_flask_wog"
    }

    stages {
        stage('Test') {
            steps {
                sh 'echo "SUCCESS" '
            }
        }
        stage('Git Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/vicefreeman/WorldOfGames.git']]])
            }
        }
    }
}
