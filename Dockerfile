ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add python2

COPY src/* /src/

CMD /usr/bin/python2 /src/pagekite-with-options.py
