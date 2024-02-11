pipeline {
      agent {dockerfile true}
    stages {
        stage('Checkout') {
            steps {
                echo 'gkl in stage - Checkout'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '0a5b6915-ce53-42e9-b665-306117ce5d98', url: 'https://github.com/mgokulm/git_pyspark_cicd_test1.git']])
            }
        }
        stage('Build') {
            steps {
                echo 'gkl in stage - Build'
                sh 'python3 jobs/ops.py'
            }
        }
      stage('Build') {
            steps {
                echo 'gkl in stage - Test'
            }
        }
    }
}
