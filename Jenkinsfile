pipeline {
  agent any
  stages {
    stage('Read and Parse Data') {
      steps {
        sh 'python3 ScoreParser.py'
      }
    }

  }
}