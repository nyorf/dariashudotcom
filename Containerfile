FROM quay.io/fedora/python-313

LABEL maintainer="me@nyorf.com"

COPY requirements.txt requirements.txt

COPY data/robots.txt data/robots.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "14300"]
