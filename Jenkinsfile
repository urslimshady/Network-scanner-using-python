node {
    // Clean workspace before doing anything
    deleteDir()
    try {

        stage ('Clone') {
            checkout scm
        }
        stage ('Build') {
            sh "echo 'shell script to build project.....!'"
        }
        stage ('tests') {
            parallel 'static': {
                sh "echo 'shell script to run static tests.....!'"
            },
            'unit': {
                sh "echo 'shell script to run unit tests.....!'"
            },
            'integration': {
                sh "echo 'shell script to run integration tests.!'"
            }
        }
        stage ('Deploy') {
            sh "echo 'shell script to deploy to server...'"
            sh "echo 'Hello there! just checking if everything is fine..'"
            sh "echo 'Done...!!!!'"
        }
    } 
	catch (err) {
        	currentBuild.result = 'FAILED'
       		throw err
    }
}
