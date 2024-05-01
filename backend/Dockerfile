FROM python:3.9
WORKDIR /app
RUN pip install flask
RUN pip install elasticsearch
RUN pip install requests
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["hello.py" ]