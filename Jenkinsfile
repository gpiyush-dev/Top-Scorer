pipeline {
  agent { docker { image '3.11.7-windowsservercore-ltsc2022' } }
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
