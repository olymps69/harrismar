import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:8000"
timeout = 120
worker_connections = 1000
accesslog = '-'
errorlog = '-'
loglevel = 'info'
graceful_timeout = 30
max_requests = 1000
max_requests_jitter = 50
preload_app = True
keepalive = 2
#gunicorn -c app/config/gunicorn_config.py app.main:app
