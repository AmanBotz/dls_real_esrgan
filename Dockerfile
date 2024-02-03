FROM python:3.9
COPY . /app/
RUN pip install -r /app/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
CMD ["python", "/app/app.py"]