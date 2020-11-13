# use the uwsgi-nginx-flask container image
# FROM tiangolo/uwsgi-nginx-flask
FROM python:alpine

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the directory at /app
ADD . /app

# install the dependencies
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
# COPY requirements.txt /tmp/
# RUN pip install --upgrade -r /tmp/requirements.txt

# COPY main.py /app/main.py
