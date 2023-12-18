# Home Assistant

## Gear
- Raspberry Pi 4 Model B

## Install homeassistant

I'm using a raspberry pi 4 model B

### Install docker (and run/test)

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ${USER}
sudo su - ${USER}

docker version
docker run hello-world
```

### Install docker-compose

```
sudo pip3 install docker-compose
```

## Run homeassistant

```
docker-compose up -d
```

## Update homeassistant

```
docker-compose pull homeassistant
```

## Remote access

Using tunnel from cloudflare informed by [this post](https://pimylifeup.com/raspberry-pi-cloudflare-tunnel/).
Creating a tunnel via the dashboard however, connecting via the code snippet presented, and installing the origin certificate from cloudflare.
