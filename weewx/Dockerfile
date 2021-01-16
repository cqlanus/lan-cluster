FROM felddy/weewx
MAINTAINER Chris Lanus <cqlanus@gmail.com>

RUN chmod -R 777 /data

RUN apt-get install wget python3-cheetah -y

# Forecast Extensions
RUN wget -O weewx-forecast.zip https://github.com/matthewwall/weewx-forecast/archive/master.zip
RUN ./bin/wee_extension --install weewx-forecast.zip

# Belchertown skin
RUN wget https://github.com/poblabs/weewx-belchertown/releases/download/weewx-belchertown-1.2/weewx-belchertown-release-1.2.tar.gz
RUN ./bin/wee_extension --install weewx-belchertown-release-1.2.tar.gz

RUN pip3 install Cheetah3
RUN mkdir /var/www && mkdir /var/www/html && mkdir /var/lib/weewx
RUN chmod -R 777 /var/lib/weewx

ENTRYPOINT ["./entrypoint.sh"]
CMD ["/data/weewx.conf"]
