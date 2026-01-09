FROM xuetangx-registry.cn-beijing.cr.aliyuncs.com/mirrors/python:3.13.5-bullseye-google-selenium

WORKDIR /root

COPY . .
RUN pip install --no-cache-dir -r requirements.txt