FROM python:3.8-slim

WORKDIR /Api

COPY . .

RUN : \
    && apt-get update \
    && pip install --no-cache-dir -r requirements.txt 
 
EXPOSE 5001

CMD ["fastapi", "run", "App", "--host", "0.0.0.0", "--proxy-headers", "--port", "5001"]

