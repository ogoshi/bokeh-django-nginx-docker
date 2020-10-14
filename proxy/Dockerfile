FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY django.conf /etc/nginx/conf.d
COPY bokeh.conf /etc/nginx/conf.d

RUN mkdir -p /var/www/media
RUN mkdir -p /var/www/static
RUN mkdir -p /var/www/templates
RUN mkdir -p /var/www/staticfiles

RUN chown -R nginx:nginx /var/www/


