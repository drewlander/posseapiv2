FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /posseapiv2
WORKDIR /posseapiv2
COPY requirements.txt /posseapiv2/
RUN pip install -r requirements.txt
COPY . /posseapiv2/

ENTRYPOINT ["/posseapiv2/entrypoint.sh"]
