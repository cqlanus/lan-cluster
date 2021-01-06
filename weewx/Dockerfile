FROM felddy/weewx:4
# FROM mitct02/weewx:3.8.0
MAINTAINER Chris Lanus <cqlanus@gmail.com>

ARG WEEWX_UID=0

RUN chmod 775 /var/lib/weewx

ENTRYPOINT ["./entrypoint.sh"]
CMD ["/data/weewx.conf"]

