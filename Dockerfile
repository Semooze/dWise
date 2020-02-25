FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements /opt/requirements
RUN pip install -r /opt/requirements

COPY ./ /app
RUN cd /app/dwise

WORKDIR /app/dwise