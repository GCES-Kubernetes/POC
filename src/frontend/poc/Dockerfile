FROM nginx:1.15.8-alpine
COPY nginx.conf /etc/nginx/nginx.conf
RUN cat /etc/nginx/nginx.conf
COPY ./dist/poc/ /usr/share/nginx/html
EXPOSE 80
