FROM nginx:latest

ADD nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/www/media
RUN mkdir -p /var/www/static
RUN mkdir -p /var/www/templates
RUN mkdir -p /var/www/staticfiles

WORKDIR /var/www/media
RUN chown -R nginx:nginx /var/www/media


WORKDIR /var/www/static
RUN chown -R nginx:nginx /var/www/static


WORKDIR /var/www/templates
RUN chown -R nginx:nginx /var/www/templates


WORKDIR /var/www/staticfiles
RUN chown -R nginx:nginx /var/www/staticfiles