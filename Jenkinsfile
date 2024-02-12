pipeline {
      agent {dockerfile true}
    stages {
        stage('Checkout') {
            steps {
                echo 'gkl in stage - Checkout'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '0a5b6915-ce53-42e9-b665-306117ce5d98', url: 'https://github.com/mgokulm/git_pyspark_cicd_test1.git']])
            }
        }
        stage('Prepare') {
            steps {
                echo 'gkl in stage - Prepare'
                sh 'pipenv install --dev'
            }
        }
        stage('Test') {
            steps {
                echo 'gkl in stage - Test'
                sh 'pipenv run pytest --html=Sample_report.html'
            }
        }
        stage('Build') {
            steps {
                echo 'gkl in stage - Build'
                sh 'python3 jobs/ops.py'
            }
        }
    }
      post {
            always {
                  echo 'gkl before publishing html'
                  publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: '', reportFiles: 'Sample_report.html', reportName: 'HTML Report', reportTitles: 'Gokuls Test report', useWrapperFileDirectly: true])
                  echo 'gkl after publishing html'
            }
      }
}
