FROM xuetangx-registry.cn-beijing.cr.aliyuncs.com/mirrors/python:3.13.5-bullseye-google-selenium

WORKDIR /root

COPY . ./xc-autotest-ui
RUN pip install --no-cache-dir -r requirements.txt