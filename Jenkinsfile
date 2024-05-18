/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('Environment Info') {
            steps {
                sh '''
                echo $PATH
                pwd
                which python3
                '''
            }
        }
        stage('Copy Credentials') {
            steps {
                sh 'cp /var/jenkins_home/data/kaggle.json /var/jenkins_home/workspace/test'
            }
        }
        stage('Create Artefacts') {
            steps {
                sh 'jupyter nbconvert --execute ecommerce.ipynb --to python'
            }
        }
        stage('Test Dataset') {
            steps {
                sh '''
                pwd
                pytest test_dataset.py
                '''
            }
        }
        stage('Deploy Application') {
            steps {
                sh 'uvicorn main:app --port 8888
            }
        
        }
    }
    post('Always run') {
        always {
            sh 'echo Pipeline has completed!'
        }
    }
}