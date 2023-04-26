FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install Jinja2==2.11.3
RUN pip install gunicorn
RUN pip install itsdangerous==2.0.1
COPY . .

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:4000"]

