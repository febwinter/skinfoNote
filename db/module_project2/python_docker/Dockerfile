# Dockerfile
FROM python:3.8.3 
WORKDIR /root
COPY . /root
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt  
RUN cat pythonAuto >> /root/.bashrc
CMD ["python3", "test.py"]