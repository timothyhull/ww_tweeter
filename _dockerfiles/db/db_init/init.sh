#!/bin/bash

# Initialization script for PostgreSQL DB

# Exit if a command returns a non-zero error code
set -e

# Export environment variables and setup database
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
  COMMIT;
  CREATE DATABASE $APP_TEST_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_TEST_DB_NAME TO $APP_DB_USER;
  COMMIT;
EOSQL
