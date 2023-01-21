importenv
export REDIS_SERVICE=localhost
export CELERY_BROKER_URL=redis://${REDIS_SERVICE}:6379/1
export CELERY_RESULT_BACKEND=redis://${REDIS_SERVICE}:6379/0
export DB_HOME=/home/shchelokovskiy/code/support_analytics/data
export SQLITE_DATABASE=/home/shchelokovskiy/code/support_analytics/data/db
export REDIS_DB=SUPPORT_ANALYTICS
export QUERY_SERVICE=localhost:11005