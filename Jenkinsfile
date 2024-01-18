pipeline {
  agent any
  stages {
    stage('Read and Parse Data') {
      steps {
        sh 'python ScoreParser.py'
      }
    }

  }
}
