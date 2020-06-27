FROM python:3.7.7-buster
# SET PORT
EXPOSE 5000
# Variables
ARG UID=1001
ARG GID=1001
ENV UID=${UID}
ENV GID=${GID}
# CREATE USER & GROUP
RUN groupadd -r --gid ${GID} app && useradd -r --uid ${UID} --gid ${GID} -s /sbin/nologin --home /app app
# CREATE FOLDERS AND PERMISSIONS
RUN mkdir /app && chown -R app:app /app
WORKDIR /app
# Copy files
COPY --chown=app:app src ./src
COPY --chown=app:app requirements.txt ./
# Install app dependencies
RUN pip install -r requirements.txt
# Change to non-privileged user
USER app
# RUN
CMD uwsgi --module src.__main__:app --http :5000 --uid ${UID} --buffer-size 32768 --post-buffering 1