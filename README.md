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
