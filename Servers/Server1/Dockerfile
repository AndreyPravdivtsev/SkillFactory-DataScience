FROM python:3.8
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./Interface1.py" ]

# to create and start
# sudo docker build -t my_server1 .
# sudo docker run -it --rm --name my_server1 my_server1


# sudo docker run -it --rm -v $PWD/src/output/:/usr/src/app/output  --name my_first_image my_first_image


# sudo docker images
# sudo docker rmi <image_id>
# sudo docker run -it --rm --name my_first_image my_first_image
# docker ps