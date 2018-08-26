ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add python2

CMD [ "python2 -c 'print \'Hello World\''" ]
