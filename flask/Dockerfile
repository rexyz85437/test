# use the python 3.8.10 container image
FROM python:3.8
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python3-dev
RUN apt-get install -y default-mysql-client
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip3 install -r requirements.txt

# run the command to start uWSGI
CMD [ "uwsgi", "app.ini" ]

