importenv
export REDIS_PORT=6379
export REDIS_SERVICE=localhost
export CELERY_BROKER_URL=redis://${REDIS_SERVICE}:6379/0
export CELERY_RESULT_BACKEND=redis://${REDIS_SERVICE}:6379/0
export DB_HOME=/home/shchelokovskiy/code/support_metrics/data
export SQLITE_DATABASE=/home/shchelokovskiy/code/support_metrics/data/db
export REDIS_DB=SUPPORT_ANALYTICS
# 0 = false, 1 = true
export UPDATE_ON_STARTUP=1
export SERVER_PORT=11001
export DEBUG=1
export RECALCULATE_FOR_LAST_DAYS=1
export RECALCULATE_FROM_THE_BEGINNING=0
export AUTH_ENABLED=0