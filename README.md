# Shadowsocks-Python-WebAPI
Python3 API (FastAPI, Uvicorn) for Shadowsocks.
You can change users list (port/password combinations) via HTTP POST response.
You need to send POST response with JSON list:
(
(int port, string password),
(43342, "jc4rkckcsf3"),
...
)

to update endpoint like:
localhost:8078/update

# Installation

Installation

1. Install deps
```
sudo apt update
sudo apt upgrade
sudo apt-get install git
sudo apt-get install nodejs
sudo apt-get install npm
sudo apt install shadowsocks-libev
sudo apt install ufw
sudo apt install python3
sudo apt install python3-pip

//to update nodejs to latest version
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
```
2. Edit .env file
3. Не забыть открыть порты
 ```
sudo ufw enable
sudo ufw allow 8078
sudo ufw allow 22
sudo ufw allow 50000:65000/tcp
sudo ufw reload
```
4. Install pip3 deps
   ```
   pip3 install fastapi uvicorn
   ```
6. Run pm2 scripts:
sudo npm install pm2 -g
```
pm2 start ~/lockshieldVPN-Sock/ss-m.sh --name "ss-manager"
pm2 start ~/lockshieldVPN-Sock/sock.py --name "sock-app" --interpreter python3
```
