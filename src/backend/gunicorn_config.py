import os

bind = os.getenv("APP_HOST", "0.0.0.0") + ":" + os.getenv("APP_PORT", "9000")
workers = os.getenv("GUNICORN_WORKERS", 1)
timeout = os.getenv("GUNICORN_TIMEOUT", 300)
keepalive = 24 * 60 * 60
threads = os.getenv("GUNICORN_THREADS", 1)