import redis

redis_host = 'localhost'
redis_port = 6379


def redis_string():
	try:
		print(f"Connecting to Redis at {redis_host}:{redis_port}")
		r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
		if r.ping():
			print("Connected to Redis")
		r.hset("uid", mapping={"name": "Farzam Asadian", "email": "farzamasadian@gmail.com"})
		msg = r.hmget("uid", ["name", "email"])
		print(msg)
	except Exception as e:
		print(e)


def redis_integer():
	try:
		print(f"Connecting to Redis at {redis_host}:{redis_port}")
		r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
		if r.ping():
			print("Connected to Redis")
		r.set("number", "100")
		o_number = r.get("number")
		r.incr("number")
		incr_number = r.get("number")
		print(o_number)
		print(incr_number)
	except redis.ConnectionError as e:
		print(f"ConnectionError: {e}")
	except Exception as e:
		print(e)


if __name__ == "__main__":
	redis_string()
	redis_integer()
