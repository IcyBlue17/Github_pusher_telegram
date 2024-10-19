FROM python:3.12-slim
WORKDIR /app
COPY . 
RUN pip3 install flask requests
CMD ["python3", "bot.py"]
