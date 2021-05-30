FROM mike0sv/sf_docker_base
WORKDIR /usr/src/app

# ENV DATA_PATH = $PWD/src/output/mytext.txt
# ENV DATA_PATH = /usr/src/app/output/mytext.txt
ENV DATA_PATH = /output/mytext.txt

COPY ./src/ .
CMD [ "python", "./writetxt.py" ]


# to create 
# sudo docker build -t secret_img .
# to start
# sudo docker run -it --rm -v $PWD/src/output/:/usr/src/app/output  --name secret_img secret_img






























# constants, variables of the container
# ENV <key>=<value>


# https://docs.docker.com/engine/reference/builder/#env
# docker ps
# docker pull
# docker build 
# docker run
# docker stop
# docker rm
# docker rmi
# docker logs
# docker kill






# sudo docker images
# sudo docker rmi <image_id>
# sudo docker run -it --rm --name my_first_image my_first_image

# docker run --env <key>=<value>