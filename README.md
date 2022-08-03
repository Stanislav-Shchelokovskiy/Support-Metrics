# How to start the app

Add **.env** file containing the following env vars:
- SQL_SERVER=..
- SQL_DATABASE=..
- SQL_USER=..
- SQL_PASSWORD=..
- APP_SERVER_PORT=11003
- FLOWER_PORT=11004
- REDIS_PORT=6379
- REDIS_URL=redis_service
- REDIS_DB=1
- CELERY_BROKER_URL=redis://redis_service:6379/1
- CELERY_RESULT_BACKEND=redis://redis_service:6379/1
- DB_HOME=/root/app/sqlite_data
- SQLITE_DATABASE=/root/app/sqlite_data/db
- CLIENT_POSTS_SQL=sql_queries/client_posts_by_tribes.sql

Make sure:
1. <b>support_analytics</b> network is created<br>
    docker network create -d bridge support_analytics
2. <b>redice_service</b> is up<br>
    docker run -d --name=redis_service --network=support_analytics -p 6379:6379 -p 11001:8001 redis/redis-stack:latest

Then run <b>docker-compose up</b>.