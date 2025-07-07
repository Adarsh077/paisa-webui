docker build -t paisa-web-ui .
docker rm -f paisa-web-ui
docker run --name paisa-web-ui --add-host=host.docker.internal:host-gateway -p 8003:8003 -d paisa-web-ui:latest