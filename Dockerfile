 FROM python:3.6
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 RUN chmod +x start.sh
 EXPOSE 8000

 CMD ["/code/start.sh"]]
