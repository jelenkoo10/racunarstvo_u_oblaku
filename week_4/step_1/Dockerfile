FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3-pip
RUN pip3 install pandas numpy scikit_learn

WORKDIR /app

ADD clean_and_preprocess.py /app/

ENTRYPOINT ["python3", "/app/clean_and_preprocess.py"]