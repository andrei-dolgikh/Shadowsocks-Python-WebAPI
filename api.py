from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from ipaddress import ip_network, ip_address
import uvicorn
from snitch import Snitch
import os
from dotenv import load_dotenv
# from fastapi.middleware.cors import CORSMiddleware

APP_API = FastAPI()
snitch = Snitch()
load_dotenv()
ip = os.getenv("IP_ADDRESS")
host = os.getenv("HOST")
port = os.getenv("PORT")
port = int(port)
method = os.getenv("METHOD")

# you can use middlevare for prod environment
# origins = [
#    "http://localhost:3000"
# ]

#APP_API.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

@APP_API.get("/status")
async def status():
    return "ok"

@APP_API.post('/update')
async def update(request: Request):
    try:
        # get ports and passwords from POST Query
        users = await request.json()
        return snitch.updateConfig(users, ip, method)
    except Exception as e:
        print(f"Configuration file updating failed - {str(e)}")
        return False

if __name__ == '__main__':
    uvicorn.run(APP_API, 
                host=host, 
                port=port, 
                # ssl_certfile=r'/www/wwwroot/certificate.crt', 
                # ssl_keyfile=r'/www/wwwroot/private.key', 
                log_level='info')
 
