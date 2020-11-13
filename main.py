from flask import Flask
import redis

app = Flask(__name__)


@app.route("/")
def say_hello():
    r = redis.Redis(
        host="redis",  # name of the redis container
        port=6379,
        decode_responses=True,
        db=0,
    )
    # r.set('foo', 'bar')
    name = r.get("name")
    return f"Hello {name}\n"


if __name__ == "__main__":
    app.run()
