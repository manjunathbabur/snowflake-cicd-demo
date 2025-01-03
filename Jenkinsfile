pipeline {
    agent any
    environment {
        SNOWSQL_PATH = '"C:\\Program Files\\Snowflake SnowSQL\\snowsql.exe"'  // Path to SnowSQL executable
        SNOWSQL_CONNECTION = 'demo'  // Connection name from SnowSQL configuration
    }
    stages {
        stage('Upload SQL Files to Snowflake Stage') {
            steps {
                script {
                    def files = [
                        'sql/demo_query.sql'  // Add additional files if needed
                        'scripts/demo_script.py'  // Add additional files if needed
                    ]
                    for (file in files) {
                        bat """
                            ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake_demo/${file.replace('\\', '/')}' @PROD_NOTEBOOK_STAGE;"
                        """
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
