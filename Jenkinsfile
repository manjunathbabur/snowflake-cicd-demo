pipeline {
    agent any
    environment {
        SNOWSQL_PATH = '"C:\\Program Files\\Snowflake SnowSQL\\snowsql.exe"'
        SNOWSQL_ACCOUNT = 'mg05545.eu-west-1'
        SNOWSQL_USER = 'MRAJAMANI'
        SNOWSQL_ROLE = 'ACCOUNTADMIN'
        SNOWSQL_WAREHOUSE = 'POC_ITIM_PERIASAMY'
        SNOWSQL_DATABASE = 'POC_CICD_PROD'
        SNOWSQL_SCHEMA = 'SH_PROD'
        SNOWSQL_STAGE = 'PROD_NOTEBOOK_STAGE'
    }
    stages {
        stage('Prompt for Password') {
            steps {
                script {
                    // Prompt for password and store it in an environment variable
                    env.SNOWSQL_PASS = input(
                        id: 'PasswordInput',
                        message: 'Enter your SnowSQL password:',
                        parameters: [password(name: 'password', description: 'SnowSQL Password')]
                    )
                }
            }
        }
        stage('Upload SQL Files') {
            steps {
                script {
                    def files = [
                        'sql/demo_query.sql'  // Add more files here if needed
                    ]
                    for (file in files) {
                        // Write the batch script dynamically
                        writeFile file: 'upload_script.bat', text: """
                            @echo off
                            ${env.SNOWSQL_PATH} -a ${env.SNOWSQL_ACCOUNT} -u ${env.SNOWSQL_USER} -p "${env.SNOWSQL_PASS}" -r ${env.SNOWSQL_ROLE} -w ${env.SNOWSQL_WAREHOUSE} -d ${env.SNOWSQL_DATABASE} -s ${env.SNOWSQL_SCHEMA} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake_demo/${file.replace('\\', '/')}' @${env.SNOWSQL_STAGE};"
                        """
                        // Execute the batch script
                        bat 'upload_script.bat'
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'SQL file(s) successfully uploaded to Snowflake stage.'
        }
        failure {
            echo 'Failed to upload SQL file(s) to Snowflake stage.'
        }
    }
}
