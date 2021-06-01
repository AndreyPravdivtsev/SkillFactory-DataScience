FROM python:3.8
WORKDIR /usr/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

# COPY ./src/ .
CMD [ "python", "./plot.py" ]

# to create and start
# sudo docker build -t my_server .
# sudo docker run -it --rm --name my_server my_server


# sudo docker run -it --rm -v $PWD/src/output/:/usr/src/app/output  --name my_first_image my_first_image


# sudo docker images
# sudo docker rmi <image_id>
# sudo docker run -it --rm --name my_first_image my_first_image
# docker ps