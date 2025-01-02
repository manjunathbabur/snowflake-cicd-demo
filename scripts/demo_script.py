import snowflake.connector

# Snowflake connection details
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account_name'
)

cursor = conn.cursor()

try:
    # Example query execution
    cursor.execute("SELECT CURRENT_VERSION();")
    for row in cursor:
        print(f"Snowflake Version: {row[0]}")
finally:
    cursor.close()
    conn.close()
