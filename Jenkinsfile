pipeline {
    agent any

    options {
        timestamps()
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
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Run E2E Tests') {
            steps {
                bat '''
                    if not exist "%REPORT_DIR%" mkdir "%REPORT_DIR%"
                    if not exist "%SCREENSHOT_DIR%" mkdir "%SCREENSHOT_DIR%"
                    docker run --rm ^
                      -e PYTHONPATH=/app ^
                      -v "%WORKSPACE%:/app" ^
                      -w /app ^
                      %IMAGE_NAME% ^
                      python -m pytest tests/e2e/test_parabank.py ^
                        --html=%REPORT_DIR%/pytest-report.html ^
                        --self-contained-html ^
                        --junitxml=%REPORT_DIR%/junit.xml ^
                        --tb=short
                '''
                archiveArtifacts artifacts: 'artifacts/**', allowEmptyArchive: true, fingerprint: true
            }
        }
    }
}
