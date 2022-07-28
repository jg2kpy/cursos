FROM python:latest
ENV PYTHONBUFFERED=1
RUN mkdir /DJANGO_WEBAPP
WORKDIR /DJANGO_WEBAPP
COPY requirements.txt* /DJANGO_WEBAPP/
RUN [ -f ./requirements.txt ] && pip install -r requirements.txt || pip install django
# COPY . /DJANGO_WEBAPP/
CMD ["bash"]