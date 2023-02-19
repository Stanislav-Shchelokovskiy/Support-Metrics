# How to start the app

Add **.env** file containing the following env vars:
- SQL_SERVER=..
- SQL_DATABASE=..
- SQL_USER=..
- SQL_PASSWORD=..
- SERVER_PORT=11003
- FLOWER_PORT=11004
- REDIS_SERVICE=redis_service
- REDIS_PORT=6379
- DB_HOME=/root/app/data
- CORS_ORIGINS=["http://ubuntu-support.corp.devexpress.com","http://localhost:3000"]
- QUERY_SERVICE=query_service_server:11005
- UPDATE_CUSTOMERS_ACTIVITY_ON_STARTUP=0

Make sure:
1. <b>support_analytics</b> network is created<br>
    docker network create -d bridge support_analytics
2. <b>redise_service</b> is up<br>
    docker run -d --name=redis_service -v redis_stack:/data --network=support_analytics -p 6379:6379 -p 10001:8001 --restart always redis/redis-stack:latest 

Then run <b>docker-compose up</b>.