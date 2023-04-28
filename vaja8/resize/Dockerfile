


FROM alpine:3.13

ADD https://github.com/openfaas/faas/releases/download/0.18.10/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

RUN apk --update add imagemagick

# Define your binary here
# ENV fprocess="/bin/cat"
ENV fprocess="convert - -resize x100 "

CMD ["fwatchdog"]