FROM node:10

ENV APP_ROOT /app/

# Application dir
WORKDIR $APP_ROOT

# copy package.json & package-lock.json
COPY package*.json $APP_ROOT

RUN npm install

# Application Bundle
COPY . $APP_ROOT