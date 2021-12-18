FROM node:current-alpine
RUN mkdir -p /home/node/app && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY ./vue_front/package*.json /home/node/app/
RUN npm install

COPY ./vue_front /home/node/app/

RUN npm run build

EXPOSE 3000
