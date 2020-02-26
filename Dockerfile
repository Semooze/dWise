FROM python:3.7

COPY requirements /opt/requirements
RUN pip install -r /opt/requirements

COPY ./ /opt
WORKDIR /opt/dwise

CMD ["uvicorn","main:app","--host","0.0.0.0", "--reload"]