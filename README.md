# docker-sample
*A simple Flask app + a Redis database*

## Simple Run with Docker

Build `flask` image and `flask-redis` network.

```bash
docker build . -t flask
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

Then, open `localhost` in your browser. You can reach the `redis` container through out the `flask` container. Check it with:


```bash
docker exec -it flask bash
ping redis
```

## Credit

- [Intro to Docker (in Persian)](https://www.youtube.com/watch?v=_jKNnHROiC0&list=PLaMA3zAw4mkQE-RDxtXZnQTb0b8KsuZ3_) by [Jadi](https://github.com/jadijadi)
