# docker-sample
*A simple Flask app + a Redis database*

## Build and Run with Docker Compose

```bash
docker-compose up -d --build --remove-orphans
curl localhost:5000
```

## Run with Docker (raw approach)

Change `Dockerfile` with:

```Dockerfile
# use the uwsgi-nginx-flask container image
FROM tiangolo/uwsgi-nginx-flask

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the directory at /app
ADD . /app

# install the dependencies
RUN pip install -r requirements.txt

# copy the runner
COPY run.py /app/main.py
```

Remove `host="0.0.0.0"` from `./flask/run.py`.

Build `flask` image and `flask-redis` network.

```bash
docker build ./flask -t flask
docker network create flask-redis
```

Create containers.

```bash
docker run --rm -it \
    --name redis \
    --network flask-redis -p 6379:6379 \
    -v /tmp/data:/data \
    redis \
    redis-server --appendonly yes

docker run --rm \
    --name flask \
    --network flask-redis -p 80:80 \
    flask
```

Then, open `localhost` in your browser (or `curl localhost`). You can reach the `redis` container through out the `flask` container. Check it with:

```bash
docker exec -it flask bash
ping redis
```

## Credit

- [Intro to Docker (in Persian)](https://www.youtube.com/watch?v=_jKNnHROiC0&list=PLaMA3zAw4mkQE-RDxtXZnQTb0b8KsuZ3_) by [Jadi](https://github.com/jadijadi)
