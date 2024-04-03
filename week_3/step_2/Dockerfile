FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3-pip
RUN pip3 install pandas scikit_learn

WORKDIR /app

ADD train_and_evaluate_model.py /app/

ENTRYPOINT ["python3", "/app/train_and_evaluate_model.py"]