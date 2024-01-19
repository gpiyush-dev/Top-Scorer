pipeline {
  agent any
  stages {
    stage('Read and Parse Data') {
      steps {
        bat 'python3 ScoreParser.py'
      }
    }

  }
}
