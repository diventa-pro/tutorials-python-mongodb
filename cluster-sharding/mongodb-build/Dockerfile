FROM mongodb/mongodb-community-server:5.0.26-ubuntu2004
USER root
COPY /auth/mongodb-keyfile /data
RUN chmod 400 /data/mongodb-keyfile
RUN chown 999:999 /data/mongodb-keyfile