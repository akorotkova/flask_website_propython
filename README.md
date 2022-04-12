clone && cd
docker build -t flaskapp .
docker run -p 5000:5000 flaskapp
