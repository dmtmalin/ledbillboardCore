```
docker build -f docker/Dockerfile -t board .
docker run -it \
    -e DB_HOST=89.223.29.124 \
    -e DB_PORT=5432 \
    -e DB_NAME=ledbillboard \
    -e DB_USER=postgres \
    -e DB_PASS=root \
    -e WEBDAV_URL=http://admin:admin@89.223.29.124:8135/ \
    -e WEBDAV_PUBLIC_URL=http://89.223.29.124:8136/ \
    board
```
Создание админа в докер-контейнере
```
docker ps
docker exec -i -t <CONTAINER ID > /bin/bash
ledbillboard createsuperuser
```
Копирование статики
```
docker cp <CONTAINER ID >:/var/www/board/static /var/www/board/static
```
