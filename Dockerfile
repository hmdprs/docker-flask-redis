FROM tiangolo/uwsgi-nginx-flask

COPY requirements.txt /tmp/
RUN pip install --upgrade -r /tmp/requirements.txt

COPY main.py /app/main.py
