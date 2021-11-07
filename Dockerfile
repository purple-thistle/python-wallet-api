FROM python:3.8

RUN python -m pip install --upgrade pip

RUN useradd --create-home wuser

#RUN mkdir /home/wuser/.pip

#COPY pip.conf /home//wuser/.pip/pip.conf

WORKDIR /home/wuser

COPY requirements.txt requirements.txt
COPY api.py api.py

USER wuser


RUN pip install --no-cache-dir -r requirements.txt --trusted-host playtikatraining.jfrog.io && rm requirements.txt

EXPOSE 5000

CMD [ "python", "./api.py" ]