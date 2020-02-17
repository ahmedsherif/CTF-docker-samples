FROM php:5-apache-stretch

RUN apt-get update \
  && docker-php-ext-install pdo pdo_mysql mysql mysqli && apt-get install unzip

COPY php.ini /usr/local/etc/php/

WORKDIR /var/www/html/
