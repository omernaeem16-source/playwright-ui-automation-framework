
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Jenkins pipeline started!'
            }
        }

        stage('Verify Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Verify Git') {
            steps {
                bat 'git --version'
            }
        }
    }
}
