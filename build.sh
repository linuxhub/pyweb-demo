#!/bin/bash


name="tools"
tag="1.0.0"
repository="docker.io/linuxhub"


image="${repository}/${name}:${tag}"
image_latest="${repository}/${name}:latest"

docker build -t ${image} .

docker tag ${image} ${image_latest}

docker push ${image}
docker push ${image_latest}

echo " "
echo "${image}"
echo "${image_latest}"
echo " "



