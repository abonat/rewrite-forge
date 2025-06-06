FROM python:3.13.3

#RUN pip3 install fastapi pydantic uvicorn[standard] python-multipart argon2-cffi

RUN mkdir /opt/rewrite-forge

COPY *.py /opt/rewrite-forge/
COPY requirements.txt /opt/rewrite-forge/
#ADD auth /opt/rewrite-forge/auth/

WORKDIR /opt/rewrite-forge/
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
