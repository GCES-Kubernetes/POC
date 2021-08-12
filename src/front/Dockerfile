### stage 1 - build 

FROM node:12.16.1-alpine As builder

WORKDIR /usr/src/app
COPY package.json package-lock.json ./

RUN npm cache clean --force

RUN npm install -g @angular/cli

RUN npm install
COPY . .
RUN npm run build --prod


FROM nginx:1.15.8-alpine
COPY nginx.conf /etc/nginx/nginx.conf
RUN cat /etc/nginx/nginx.conf
COPY --from=builder /usr/src/app/dist/front/ /usr/share/nginx/html
EXPOSE 80
