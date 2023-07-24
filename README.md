# How to start the app

Add **.env** file containing the following env vars:
- SQL_SERVER=..
- SQL_DATABASE=..
- SQL_USER=..
- SQL_PASSWORD=..
- REDIS_SERVICE=redis_service
- REDIS_PORT=6379
- DB_HOME=/root/app/data
- CORS_ORIGINS=["https://ubuntu-support.corp.devexpress.com","http://localhost:3000"]
- QUERY_SERVICE=http://query_service
- UPDATE_ON_STARTUP=0
- PRODUCTION=1

Make sure:
1. <b>support_analytics</b> network is created<br>
    docker network create -d bridge support_analytics
2. <b>redise_service</b> is up<br>
    docker run -d --name=redis_service -v redis_stack:/data --network=support_analytics --restart always redis/redis-stack:latest 

Then run <b>docker-compose up</b>.