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

## Installing certificate

Create a self signed certificate from letsencrypt
```
certbot-auto certonly --standalone --preferred-challenges http-01 --email your@email.com -d custom.duckdns.org
```

Copy the required files to your homeassistant
```
sudo cp /etc/letsencrypt/live/custom.duckdns.org/fullchain.pem fullchain.pem
sudo cp /etc/letsencrypt/live/custom.duckdns.org/privkey.pem privkey.pem
```
