## Setup Docker Enviroment
- install docker
    - [Docker Engine overview](https://docs.docker.com/install/)
- install docker compose
    - [Install Docker Compose](https://docs.docker.com/compose/install/)
## Create node application
```
$ mkdir <work dir>
$ npm init -y
$ npm i express
$ npm i typescript @types/express
$ ./node_modules/.bin/tsc --init
$ mkdir dist
$ npm run tsc
```
## Create dockerfile & docker-compose
```
$ touch dockerfile
$ touch docker-compose.yml
```
## Run application on docker
```
$ git clone https://github.com/gisaburo/SOA.git
$ cd SOA/iac/docker/nodejs
$ npm install
$ docker-compose up --build web
```