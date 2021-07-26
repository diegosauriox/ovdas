FROM python:3-alpine
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN pip3 install pyrocko
COPY . /code/
EXPOSE 8000
CMD ["./manage.py", "runserver"]