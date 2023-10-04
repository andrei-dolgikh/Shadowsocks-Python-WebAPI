import json
import subprocess

class Snitch(object):
    def __init__(self):
        self.config_file = "/etc/shadowsocks-libev/config.json"

    # generate config file shadowsocks
    def generateConfig(self, users, ip, method):
        config = {
            "server": f"{ip}",
            "port_password": {},
            "timeout": 15,
            "method": f"{method}",
        }
        for user in users:
            port = user[0]
            password = user[1]
            config['port_password'][port] = password
        return config
    
    # update config file and restart server
    def updateConfig(self, users, ip, method):
        usersCount = len(users)
        config = self.generateConfig(users, ip, method)
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)

        command = "pm2 restart ss-manager"
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        stdout = result.stdout.decode("utf-8")

        if result.returncode == 0:
            print("Updated. Users: ", usersCount)
            return True
        else:
            print("Error in process of update. ", result.stderr.decode("utf-8"))
            return False
