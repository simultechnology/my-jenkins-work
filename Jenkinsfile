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
                    apt-get update && apt-get install -y curl
                    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
                    $HOME/.poetry/bin/poetry install --no-root
                    poetry install
                    poetry run isort src
                    """
                }
            }
        }
    }
}
