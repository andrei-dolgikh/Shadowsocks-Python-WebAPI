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

You can edit this host and port in .env file.

You need to install Node.JS and PM2 proccess manager and create proccess by command: pm2 start *path to your repository*/start_ss_manager.sh --name "ss-manager"
Show app logs: pm2 logs ss-manager
Restart app: pm2 restart ss-manager

If you dont like to use Node and pm2, you can take a direct python3 command from start_ss_manager.py.
In this case you would be change restart command in snitch.py, because command in this file used for pm2.

This API use shadowsocks-libev now. But it can works for any build, if it is possible to change users list via config file.
