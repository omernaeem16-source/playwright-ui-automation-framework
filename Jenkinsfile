
pipeline {
    agent any

    environment {
        QA_USERNAME = credentials('qa-demo-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Jenkins pipeline started!'
            }
        }

        stage('Verify Environment') {
            steps {
                bat 'python --version'
                bat 'git --version'
                bat 'python -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat 'python -m playwright install chromium'
            }
        }

        stage('Check Credentials') {
            steps {
                bat 'if defined QA_USERNAME (echo QA_USERNAME is set) else (echo QA_USERNAME is missing)'
                bat 'if defined QA_USERNAME_PSW (echo QA_USERNAME_PSW is set) else (echo QA_USERNAME_PSW is missing)'
                bat 'if defined QA_PASSWORD (echo QA_PASSWORD is set) else (echo QA_PASSWORD is missing)'
            }
        }

        stage('Run Playwright Tests') {
            environment {
                QA_PASSWORD = "${QA_USERNAME_PSW}"
            }

            steps {
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline execution completed.'
        }

        success {
            echo 'All pipeline stages completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
