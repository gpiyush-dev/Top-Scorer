pipeline {
  docker { image 'python:latest' }
  stages {
    stage('Read and Parse Data') {
      steps {
        sh 'python ScoreParser.py'
      }
    }

  }
}
