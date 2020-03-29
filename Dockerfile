FROM python:3.5.8-alpine3.9
COPY . /app
WORKDIR /app
RUN set -xe \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache bash git openssh \
    && apk add --no-cache vim mysql-client nss curl bind-tools libcurl net-tools iproute2 drill busybox-extras nmap coreutils\
    && apk add --no-cache bash bash-doc bash-completion \
    && pip install -r ./requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 5000

CMD ["python","main.py"]
