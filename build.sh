#!/bin/bash

# 镜像名称和标签
IMAGE=deploy.deepexi.com/console-tag/gpt-server
IMAGE_TAG=1.0.1

# Dockerfile文件位置
DOCKERFILE_PATH=./Dockerfile

# Docker注册表URL和凭据 
REGISTRY_URL=https://deploy.deepexi.com
REGISTRY_PROJECT=console-tag
REGISTRY_USER=myusername
REGISTRY_PASSWORD=mypassword

# 构建上下文(仅当Dockerfile不在当前目录时需要)
# BUILD_CONTEXT=./

# 测试Dockerfile语法
echo "Checking Dockerfile syntax..." 
docker run -i hadolint/hadolint hadolint < $DOCKERFILE_PATH

# 构建镜像
echo "清理本地 env包"
rm -fr env

# 构建镜像
echo "Building image: "${IMAGE}:${IMAGE_TAG}
docker build ${BUILD_CONTEXT} -t ${IMAGE}:${IMAGE_TAG} -f $DOCKERFILE_PATH .

# 推送到注册表
echo "Pushing to registry..."
docker push ${IMAGE}:${IMAGE_TAG}

# 登录到注册表(如果尚未登录)
# echo "Logging into registry..."
# docker login -u $REGISTRY_USER -p $REGISTRY_PASSWORD $REGISTRY_URL  

echo "Build and push complete!"