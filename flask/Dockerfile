# use the uwsgi-nginx-flask container image
FROM python:alpine

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the directory at /app
ADD . /app

# install the dependencies
RUN pip install -r requirements.txt

# the runner
CMD ["python", "run.py"]
