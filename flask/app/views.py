from redis import Redis

from app import app


@app.route("/")
def index():
    redis = Redis(
        host="redis",  # name of the redis container
        port=6379,
        decode_responses=True,
        db=0,
    )
    # r.set('foo', 'bar')
    count = redis.incr("hits")
    name = redis.get("name")
    return f"Hello {name}! I have been seen {count} times.\n"
