#!/bin/bash

# 容器名
NAME=gbt4-server

# 镜像名称
IMAGE=deploy.deepexi.com/console-tag/gpt-server
IMAGE_TAG=$IMAGE_TAG

# 设置容器路径和端口映射
# CONTAINER_DIR=/opt
# HOST_DIR=$HOME/share
PORT=8000:8000

# 如果容器正在运行,停止它 
if docker ps -a | grep $NAME; then
    echo "Stopping container..."
    docker stop $NAME
    docker rm $NAME
fi

# # 如果映射的主机目录不存在,创建它 
# if [ ! -d $HOST_DIR ]; then
#     echo "Creating host directory..." 
#     mkdir -p $HOST_DIR
# fi

# 启动容器  -v $HOST_DIR:$CONTAINER_DIR \
echo "Starting container..."
docker run -d --name $NAME \
           -p $PORT \
           $IMAGE:${IMAGE_TAG}

# 容器启动并打印日志
echo "Container started!"
docker logs -f $NAME 
