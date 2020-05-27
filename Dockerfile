FROM centos:latest
RUN yum update -y
RUN yum install python36 -y
RUN yum install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow==2.0.0
RUN pip3 install keras
WORKDIR /model
COPY mnist_cnn.py /model
COPY mnist_sklearn.py /model
COPY mnist_cnn_update.py /model
CMD python3 mnist_cnn.py