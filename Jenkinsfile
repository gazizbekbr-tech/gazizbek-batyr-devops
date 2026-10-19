pipeline {
    agent any

    environment {
        STUDENT_NAME    = 'Batyr'
        STUDENT_SURNAME = 'Gazizbek'
        STUDENT_GROUP   = 'IT2-2301'
        STUDENT_ID      = '38091'
        IMAGE_NAME      = 'gazizbek-batyr-devops'
        CONTAINER_NAME  = 'gazizbek-batyr-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "Commit used by Jenkins:" && git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "Student: $STUDENT_NAME $STUDENT_SURNAME"
                    echo "Group: $STUDENT_GROUP"
                    echo "Student ID: $STUDENT_ID"
                    python3 -m py_compile app/app.py
                    chmod +x scripts/*.sh
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    test -f Gazizbek_Batyr_info.txt
                    bash -n scripts/Gazizbek_Batyr_system.sh
                    python3 app/test_app.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER -t $IMAGE_NAME:latest .'
                sh 'docker images $IMAGE_NAME'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME \
                        -e STUDENT_NAME=$STUDENT_NAME \
                        -e STUDENT_SURNAME=$STUDENT_SURNAME \
                        -e STUDENT_GROUP=$STUDENT_GROUP \
                        -e STUDENT_ID=$STUDENT_ID \
                        $IMAGE_NAME:latest
                    sleep 3
                    docker ps --filter name=$CONTAINER_NAME
                    docker logs $CONTAINER_NAME
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully!' }
        failure { echo 'Pipeline failed - check the stage logs above.' }
    }
}
