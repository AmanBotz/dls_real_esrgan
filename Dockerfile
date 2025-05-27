FROM python:3.9
COPY . .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
EXPOSE 8000
CMD ["python", "server.py"]
