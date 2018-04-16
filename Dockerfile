FROM mm-core

WORKDIR /wagtail

COPY . .

EXPOSE 8000 80

#ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
