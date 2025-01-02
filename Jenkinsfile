pipeline {
    agent any
    environment {
        SNOWSQL_PATH = '"C:\\Program Files\\Snowflake SnowSQL\\snowsql.exe"'  // Adjust to the correct SnowSQL path
        SNOWSQL_ACCOUNT = 'mg05545.eu-west-1'
        SNOWSQL_USER = 'MRAJAMANI'
        SNOWSQL_ROLE = 'ACCOUNTADMIN'
        SNOWSQL_WAREHOUSE = 'POC_ITIM_PERIASAMY'
        SNOWSQL_DATABASE = 'POC_CICD_PROD'
        SNOWSQL_SCHEMA = 'SH_PROD'
        SNOWSQL_STAGE = 'PROD_NOTEBOOK_STAGE'
    }
    stages {
        stage('Upload SQL Files') {
            steps {
                withCredentials([string(credentialsId: 'SNOWSQL_PASSWORD', variable: 'PASSWORD')]) {
                    script {
                        def files = [
                            'sql/demo_query.sql'  // Add more files as needed
                        ]
                        for (file in files) {
                            bat """
                                ${env.SNOWSQL_PATH} -a ${env.SNOWSQL_ACCOUNT} -u ${env.SNOWSQL_USER} -p "${PASSWORD}" -r ${env.SNOWSQL_ROLE} -w ${env.SNOWSQL_WAREHOUSE} -d ${env.SNOWSQL_DATABASE} -s ${env.SNOWSQL_SCHEMA} -q \"
                                PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake_demo/${file.replace('\\', '/')}' @${env.SNOWSQL_STAGE};\"
                            """
                        }
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
