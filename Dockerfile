# Use a base image with Python and Node.js pre-installed
FROM node:latest

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    git \
    npm \
    shadowsocks-libev \
    ufw \
    python3 \
    python3-pip \
    pm2

# Copy the application code to the container
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip3 install fastapi uvicorn

# Expose necessary ports
EXPOSE 8078
EXPOSE 22
EXPOSE 50000-65000

# Start the application
CMD ["pm2", "start", "ss-m.sh", "--name", "ss-manager", "&&", "pm2", "start", "sock.py", "--name", "sock-app", "--interpreter", "python3"]