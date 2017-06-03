```
docker build -f docker/Dockerfile -t board .
docker run -it \
    -e DB_HOST=192.168.2.135 \
    -e DB_PORT=5432 \
    -e DB_NAME=ledbillboard \
    -e DB_USER=postgres \
    -e DB_PASS=root \
    -e WEBDAV_URL=172.17.0.2 \
    -e WEBDAV_PUBLIC_URL=172.17.0.2 \
    board
```
Создание админа в докер-контейнере
```
docker ps
docker exec -i -t <CONTAINER ID > /bin/bash
ledbillboard createsuperuser
```
