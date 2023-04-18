node {
    // Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
            checkout scm
        }
        stage ('Build') {
            sh "echo 'shell scripts to build project..!'"
        }
        stage ('Tests') {
            parallel 'static': {
                sh "echo 'shell scripts to run static tests.!'"
            },
            'unit': {
                sh "echo 'shell scripts to run unit tests.!'"
            },
            'integration': {
                sh "echo 'shell scripts to run integration tests.!'"
            }
        }
        stage ('Deploy') {
            sh "echo 'shell scripts to deploy to server...'"
            sh "echo 'Hello there! just checking if everything is fine..'"
            sh "echo 'Done........!!!!'"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
