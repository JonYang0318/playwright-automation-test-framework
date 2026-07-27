pipeline {
    agent any

    options {
        timestamps()
        ansiColor('xterm')
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'demo-bank-e2e:jenkins'
        REPORT_DIR = 'artifacts/reports'
        SCREENSHOT_DIR = 'artifacts/screenshots'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Run E2E Tests') {
            steps {
                sh 'mkdir -p ${REPORT_DIR} ${SCREENSHOT_DIR}'
                sh '''
                    docker run --rm \
                      -u $(id -u):$(id -g) \
                      -e PYTHONPATH=/app \
                      -v "$PWD":/app \
                      -w /app \
                      ${IMAGE_NAME} \
                      python -m pytest tests/e2e/test_parabank.py \
                        --html=${REPORT_DIR}/pytest-report.html \
                        --self-contained-html \
                        --junitxml=${REPORT_DIR}/junit.xml \
                        --tb=short
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'artifacts/reports/junit.xml'
                    publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'artifacts/reports',
                        reportFiles: 'pytest-report.html',
                        reportName: 'Pytest HTML Report'
                    ])
                    archiveArtifacts artifacts: 'artifacts/**', allowEmptyArchive: true, fingerprint: true
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
