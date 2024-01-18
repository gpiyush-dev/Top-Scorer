pipeline {
  agent { docker { image 'python:latest' } }
  environment {
      DOCKER_HOST = 'tcp://localhost:2375'
  }
  stages {
    stage('Read and Parse Data') {
      steps {
        sh 'python ScoreParser.py'
      }
    }

  }
}
