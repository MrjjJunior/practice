# Docker


## Permission
This grants permission to use docker on a unix system.

```
sudo usermod -aG docker $USER
newgrp docker
```

## Images
vision snapshots that have all the dependencies and configs need for the application.
it is a blue print.
how to list available docker images
```
docker images
```

REPOSITORY -> Image name
TAG -> Version
IMAGE ID -> Unique Identifier 
SIZE -> How much space it uses 

### Get an ubuntu image

Downloading a linux environment
```
docker pull ubuntu
```



## Containers
running instance of that image.  

You check them using
```
docker ps -a
```
ps: process status
-a: All

### Creating a container 

```
docker run -it ubuntu
```
docker: Docker cli 
run: create and start 
-it: interactive terminal 
Interactivte terminal inside this container
ubuntu: image 
ubuntu is the image we want to use.

### Creating without starting container

```
docker create --name <name of container> ubuntu
```


check ubuntu information 
```
cat /etc/os-release
```

### Starting a container

This will start the process 
```
docker start <container id >
```
This will take you to the terminal of the container
 
### Docker Networking




