FROM alpine:3.10

RUN apk add --no-cache git curl jq bash

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]