pipeline {
  agent {
    docker { image 'python:latest' }
  }
  stages {
    stage('Read and Parse Data') {
      steps {
        sh 'python3 ScoreParser.py'
      }
    }

  }
}
