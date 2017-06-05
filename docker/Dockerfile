# Use an official Python runtime as a base image
FROM python:3.5.3
MAINTAINER Dmtmalin <dmt.malin@gmail.com>
# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1
# Install some necessary things.
RUN apt-get update
RUN apt-get install -y gettext
# Install uWSGI
RUN pip install uwsgi==2.0.15
# Set the working directory to /app
WORKDIR /app
# Copy the previous directory contents into the container at /app
ADD . /app
# Install application and static components
RUN python setup.py install
# Collect static files
ADD docker/make_static.sh /
RUN chmod +x /make_static.sh
# Compilile i18n messages
RUN ledbillboard compilemessages
# Make port 8000 available to the world outside this container
EXPOSE 8000
# Run script
ADD docker/run.sh /
CMD ["/run.sh"]