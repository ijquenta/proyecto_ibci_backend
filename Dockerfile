FROM python:3.10.12-slim-buster
RUN pip install gunicorn
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY app/ /app
WORKDIR /app
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5000","--timeout", "2000", "--access-logfile", "access.log", "--error-logfile", "error.log", "--preload","wsgi:app"] 