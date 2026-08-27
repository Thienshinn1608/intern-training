from flask import Flask, jsonify
import redis
import time
import json

app = Flask(__name__)

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def query_database():
    time.sleep(0.5)

    return [
        {
            "id": 1,
            "name": "Lipstick",
            "price": 250000
        },
        {
            "id": 2,
            "name": "Cleanser",
            "price": 180000
        },
        {
            "id": 3,
            "name": "Sunscreen",
            "price": 300000
        }
    ]


@app.route("/products/no-cache")
def no_cache():

    start = time.perf_counter()

    products = query_database()

    end = time.perf_counter()

    response_time = (end - start) * 1000

    return jsonify({
        "test": "WITHOUT REDIS",
        "source": "database",
        "responseTime": f"{response_time:.2f} ms",
        "data": products
    })


@app.route("/products/cache")
def with_cache():

    start = time.perf_counter()

    cache_key = "products"

    cached_data = r.get(cache_key)

    # CACHE HIT
    if cached_data:

        end = time.perf_counter()

        response_time = (end - start) * 1000

        return jsonify({
            "test": "WITH REDIS",
            "cache": "HIT",
            "source": "redis",
            "responseTime": f"{response_time:.2f} ms",
            "data": json.loads(cached_data)
        })

    # CACHE MISS
    products = query_database()

    r.setex(
        cache_key,
        60,
        json.dumps(products)
    )

    end = time.perf_counter()

    response_time = (end - start) * 1000

    return jsonify({
        "test": "WITH REDIS",
        "cache": "MISS",
        "source": "database",
        "responseTime": f"{response_time:.2f} ms",
        "data": products
    })


if __name__ == "__main__":

    try:
        r.ping()
        print("Redis connected!")
    except redis.ConnectionError:
        print("Cannot connect to Redis")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )