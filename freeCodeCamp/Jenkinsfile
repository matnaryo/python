pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'git@github.com:USERNAME/NAMA_REPO.git',
                    credentialsId: 'github-ssh'
            }
        }
        stage('Run') {
            steps {
                sh 'python3 luas_trapesium.py'
            }
        }
    }
}
