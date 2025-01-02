# Snowflake CI/CD Demo

This repository demonstrates a CI/CD pipeline to deploy `.sql` and `.py` files to Snowflake's `PROD_NOTEBOOK_STAGE`.

## Structure
- `sql/`: Contains SQL scripts.
- `scripts/`: Contains Python scripts.
- `tests/`: Contains unit tests.
- `Jenkinsfile`: Defines the CI/CD pipeline.

## Setup
1. Configure SnowSQL with your Snowflake credentials.
2. Update the `Jenkinsfile` with your Snowflake account details.
3. Push the repository to a Git server.

## Deployment
The pipeline uploads files to the `PROD_NOTEBOOK_STAGE` in Snowflake.

