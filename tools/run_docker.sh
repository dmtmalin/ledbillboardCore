docker run -dit \
    -e DB_HOST=89.223.29.124 \
    -e DB_PORT=5432 \
    -e DB_NAME=ledbillboard \
    -e DB_USER=postgres \
    -e DB_PASS=root \
    -e WEBDAV_URL=http://admin:admin@89.223.29.124:8135/ \
    -e WEBDAV_PUBLIC_URL=http://89.223.29.124/ \
    board