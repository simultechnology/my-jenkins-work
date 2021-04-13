pipeline {
    agent any
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!'
            }
        }
        stage('poetry run') {
            steps {
                script {
                    sh """
                    poetry install
                    poetry run isort src
                    """
                }
            }
        }
    }
}
