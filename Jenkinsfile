pipeline {
    agent any
    environment {
        SNOWSQL_ACCOUNT = 'mg05545.eu-west-1'
        SNOWSQL_USER = 'MRAJAMANI'
        SNOWSQL_ROLE = 'ACCOUNTADMIN'
        SNOWSQL_WAREHOUSE = 'POC_ITIM_PERIASAMY'
        SNOWSQL_DATABASE = 'POC_CICD_PROD'
        SNOWSQL_SCHEMA = 'SH_PROD'
        SNOWSQL_STAGE = 'PROD_NOTEBOOK_STAGE'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/manjunathbabur/snowflake-cicd-demo.git'
            }
        }
       stage('Install Snowflake Connector') {
    steps {
        bat 'pip install snowflake-connector-python'
    }
}

        stage('Upload Files to Stage') {
            steps {
                script {
                    bat "snowsql -a %SNOWSQL_ACCOUNT% -u %SNOWSQL_USER% -r %SNOWSQL_ROLE% -w %SNOWSQL_WAREHOUSE% -d %SNOWSQL_DATABASE% -s %SNOWSQL_SCHEMA% -q \"PUT 'file://%cd%\\sql\\demo_query.sql' @%SNOWSQL_STAGE%;\""
                    bat "snowsql -a %SNOWSQL_ACCOUNT% -u %SNOWSQL_USER% -r %SNOWSQL_ROLE% -w %SNOWSQL_WAREHOUSE% -d %SNOWSQL_DATABASE% -s %SNOWSQL_SCHEMA% -q \"PUT 'file://%cd%\\scripts\\demo_script.py' @%SNOWSQL_STAGE%;\""
                }
            }
        }
    }
    post {
        success {
            echo 'Files successfully uploaded to the stage.'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
