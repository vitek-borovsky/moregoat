FROM python:3.11

WORKDIR /app

COPY src/ /app/src/

RUN python -m pip install --no-cache-dir \
    -i https://pypi.org/simple \
    flask \
    flask-socketio \
    simple-websocket \
    eventlet \
    pytest

EXPOSE 5000

ENTRYPOINT [ "python", "src/main.py" ]
