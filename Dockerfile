FROM centos:latest

RUN yum install python36 -y
RUN pip3 install --upgrade pip setuptools
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install pillow

CMD ["python3","/MLops/testing.py"]
