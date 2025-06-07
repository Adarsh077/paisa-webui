docker build -t paisa-web-ui .
docker remove paisa-web-ui -f
docker run --name paisa-web-ui --add-host=host.docker.internal:host-gateway -p 8003:8003 -d paisa-web-ui:latest