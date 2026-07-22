import os

from flask import Flask
from redis import Redis

app = Flask(__name__)

redis_client = Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
)


@app.route("/")
def home():
    count = redis_client.incr("page_hits")
    return f"Hello from Docker Compose! Page viewed {count} time(s).\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)