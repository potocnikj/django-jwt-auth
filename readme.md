== Developement ==
Project is dockerized. In order to start developement:

1. change directory to project root
2. install docker.io
3. add $USER to docker group
4. `docker build -t django-jwt-auth .`
5. `docker run -d -p [OUTSIDE_PORT]:8000 -v [FULL_PATH_TO_PROJECT_ROOT]:/code django-jwt-auth`

6. `docker ps` will give you information about your docker ID's

7. `docker stop [CONTAINER_ID]` will stop your container
