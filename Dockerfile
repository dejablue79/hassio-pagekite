ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add python3

COPY src/* /src/

CMD /usr/bin/python3 /src/pagekite-with-options.py
