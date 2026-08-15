pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        PROJECT_NAME = 'Python Calculator'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "=========================================="
                    echo "Checking out source code from repository..."
                    echo "=========================================="
                }
                checkout scm
                script {
                    echo "Source code checkout completed successfully"
                    sh 'git log -1 --oneline'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "=========================================="
                    echo "Installing Python dependencies..."
                    echo "=========================================="
                }
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    echo "Dependencies installed successfully"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "=========================================="
                    echo "Running pytest test suite..."
                    echo "=========================================="
                }
                sh '''
                    pytest test_calculator.py -v --tb=short --junit-xml=test-results.xml --cov=a --cov=b --cov-report=html
                    echo "Test suite execution completed"
                '''
            }
        }

        stage('Run Calculator Code') {
            steps {
                script {
                    echo "=========================================="
                    echo "Running calculator demonstrations..."
                    echo "=========================================="
                }
                sh '''
                    echo "Running basic calculator demonstrations:"
                    python a.py
                    echo ""
                    echo "Calculator code executed successfully"
                '''
            }
        }
    }

    post {
        always {
            script {
                echo "=========================================="
                echo "Post-build operations: Collecting reports..."
                echo "=========================================="
            }
            // Publish test results
            junit testResults: 'test-results.xml', allowEmptyResults: true
            
            // Publish code coverage report
            publishHTML([
                reportDir: 'htmlcov',
                reportFiles: 'index.html',
                reportName: 'Code Coverage Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true
            ])
            
            // Archive test results and coverage
            archiveArtifacts artifacts: 'test-results.xml, htmlcov/**', allowEmptyArchive: true
        }

        success {
            script {
                echo "=========================================="
                echo "✓ Pipeline execution SUCCESSFUL"
                echo "=========================================="
            }
            // You can add email notification here
            // emailext(
            //     to: 'team@example.com',
            //     subject: "Jenkins Build Success: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
            //     body: "Build completed successfully.\nBuild URL: ${env.BUILD_URL}"
            // )
        }

        failure {
            script {
                echo "=========================================="
                echo "✗ Pipeline execution FAILED"
                echo "=========================================="
            }
            // You can add email notification here
            // emailext(
            //     to: 'team@example.com',
            //     subject: "Jenkins Build Failure: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
            //     body: "Build failed. Please review the logs.\nBuild URL: ${env.BUILD_URL}"
            // )
        }

        unstable {
            script {
                echo "=========================================="
                echo "⚠ Pipeline execution UNSTABLE"
                echo "=========================================="
            }
        }

        cleanup {
            script {
                echo "Cleaning up workspace..."
            }
            deleteDir()
        }
    }
}
