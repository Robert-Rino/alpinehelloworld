FROM         python:3.9.7-alpine3.14 as builder
ADD         ./webapp/requirements.txt requirements.txt
RUN         pip install --no-cache-dir -qr requirements.txt


FROM        python:3.9.7-alpine3.14
COPY        --from=builder /usr/local /usr/local

ADD         ./webapp /opt/webapp/
WORKDIR     /opt/webapp
			
CMD         gunicorn --bind 0.0.0.0:$PORT wsgi --log-level "debug" 

