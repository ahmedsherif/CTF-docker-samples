## Docker templates for CTF challenges


In each folder, you will be able to run and modify the `docker-compose.yml` file based on your needs.

container name:

You can change the container name based on the `container_name` option:

```yaml
version: '3'
services:
   web:
     container_name: "flask_vuln"
     build: .
     ports:
       - "127.0.0.1:5000:5000"
```

## Get the nginx configuration (list the challenges and subdomains)

by running the following command directly:

```
python ctf-nginx-add.py
```

Add new challenge to nginx: 

```
python ctf-nginx-add.py /etc/letsencrypt/live/ctf.sherif.ninja/fullchain.pem /etc/letsencrypt/live/ctf.sherif.ninja/privkey.pem ctf.sherif.ninja 8443

```
