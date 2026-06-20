FROM redhat/ubi9:latest
LABEL maintainer="dishant@gmail.com"
LABEL author="dishant"
LABEL name="PYTHON CODE IN HTTPD"
ENV App_name=" ROCK_PAPER_SCISSOR"
RUN yum install httpd python3 -y
RUN rm -f /etc/httpd/conf.d/welcome.conf
RUN touch /etc/httpd/conf.d/cgi.conf
WORKDIR /var/www/cgi-bin
COPY game.py /var/www/cgi-bin/game.py
COPY cgi.conf /etc/httpd/conf.d/cgi.conf
RUN chmod 755 game.py
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
