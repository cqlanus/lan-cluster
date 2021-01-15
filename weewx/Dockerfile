FROM ubuntu:20.04
# FROM mitct02/weewx:3.8.0
MAINTAINER Chris Lanus <cqlanus@gmail.com>

RUN apt update
RUN apt install wget python3-configobj python3-pil python3-serial python3-usb python3-pip python3-ephem -y
RUN apt install python3-cheetah -y

RUN wget https://weewx.com/downloads/weewx-4.3.0.tar.gz
RUN tar xvfz weewx-4.3.0.tar.gz
WORKDIR weewx-4.3.0

RUN python3 ./setup.py build
RUN python3 ./setup.py install

RUN cd /home/weewx
RUN cp util/init.d/weewx.debian /etc/init.d/weewx
RUN chmod +x /etc/init.d/weewx
RUN update-rc.d weewx defaults 98

CMD /etc/init.d/weewx start
