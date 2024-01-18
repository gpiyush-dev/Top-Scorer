pipeline {
  agent { label 'mymachine' }
  stages {
    stage('Read and Parse Data') {
      steps {
        sh 'python ScoreParser.py'
      }
    }

  }
}
