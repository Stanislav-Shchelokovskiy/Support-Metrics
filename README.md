# How to start the app

Add **.env** file containing the following env vars:
- SQL_SERVER=..
- SQL_DATABASE=..
- SQL_USER=..
- SQL_PASSWORD=..
- APP_SERVER_PORT=11003
- FLOWER_PORT=11004
- CELERY_BROKER_URL=redis://redis_service:6379/0
- CELERY_RESULT_BACKEND=redis://redis_service:6379/0
- DB_HOME=/root/app/user_posts_data
- SQLITE_DATABASE=/root/app/user_posts_data/db
- USER_POSTS_SQL=sql_queries/user_posts_by_tribes.sql
- USER_POSTS_TABLE_NAME=user_posts_by_tribe

Make sure:
1. <b>support_analytics</b> network is created<br>
    docker network create -d bridge support_analytics
2. <b>redice_service</b> is up<br>
    docker run -d --name=redis_service --network=support_analytics -p 6379:6379 -p 11001:8001 redis/redis-stack:latest

Then run <b>docker-compose up</b>.