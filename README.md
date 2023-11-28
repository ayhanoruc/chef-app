# chef-app
this is the future of COOKING-COPILOT APPS

- Start Docker engine
- `docker build -t chefapp-fastapi .`
- `docker run -p 8000:8000 chefapp-fastapi` 
- push the image to DockerHub

Digital Ocean Server
----
- create ssh private-public keys: `ssh-keygen -t rsa`
- enter passphrase if needed
- check the public key: 
    [`cd %USERPROFILE%\.ssh`] then [`type id_rsa.pub`]
- copy this public key, and create droplet using this ssh as credential instead of username-password
- after initializing the droplet you can connect to the server by: `ssh root@ip_adress`
