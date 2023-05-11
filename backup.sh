#!/bin/bash

# MySQL connection details
DB_HOST="localhost"
DB_USER="root"
DB_PASS="4922"
DB_NAME="sys"

# Backup file name and path
BACKUP_FILE="database_backup.sql"

# Export the MySQL database
mysqldump --host=$DB_HOST --user=$DB_USER --password=$DB_PASS $DB_NAME > $BACKUP_FILE

# Display backup completion message
echo "Database backup completed: $BACKUP_FILE"
