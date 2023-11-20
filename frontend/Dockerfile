
FROM node:21-alpine

WORKDIR /usr/src/app

COPY app/package.json ./

RUN npm install

COPY app /usr/src/app/

#RUN npm run build

EXPOSE 9000

CMD ["npm", "run", "dev"]