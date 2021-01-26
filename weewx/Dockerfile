FROM felddy/weewx
MAINTAINER Chris Lanus <cqlanus@gmail.com>

RUN chmod -R 777 /data

RUN apt-get install wget python3-cheetah -y

# Forecast Extensions
RUN wget -O weewx-forecast.zip https://github.com/cqlanus/weewx-forecast/archive/master.zip
RUN ./bin/wee_extension --install weewx-forecast.zip

# Belchertown skin
RUN wget https://github.com/poblabs/weewx-belchertown/releases/download/weewx-belchertown-1.2/weewx-belchertown-release-1.2.tar.gz
RUN ./bin/wee_extension --install weewx-belchertown-release-1.2.tar.gz

RUN mkdir /var/lib/weewx
RUN chmod -R 777 /var/lib/weewx

RUN apt update
RUN apt install nginx -y
COPY ./nginx/weewx.conf /etc/nginx/sites-available/weewx.conf
RUN ln -s /etc/nginx/sites-available/weewx.conf /etc/nginx/sites-enabled/weewx.conf
EXPOSE 8001/tcp
RUN service nginx start
RUN cd ~
RUN python -m pip install pip
RUN apt-get install zlib1g-dev libjpeg-dev build-essential -y
RUN python -m pip install Cheetah3
RUN python -m pip install Pillow

RUN sed -i -e 's/isAlive/is_alive/g' `find /home/weewx -name '*.py'`
RUN cd /home/weewx
COPY ./skins /home/weewx/skins/

ENTRYPOINT ["./entrypoint.sh"]
CMD ["/data/weewx.conf"]
