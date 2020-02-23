#!/usr/bin/python3
import random,string
import sys,re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_challenges(ssl_certificate,ssl_certificate_key,domain,docker_port):
    nginx_path = '/etc/nginx/sites-enabled/default'
    random_name = randomString(10)
    server_config = '''server {{
        listen 443 ssl;
        ssl_certificate {0};
        ssl_certificate_key {1};
    server_name {2}.{3};
            location / {{
                proxy_set_header X-Real-IP $remote_addr;
                 proxy_set_header X-Forwarded-For $remote_addr;
                 proxy_set_header Host $host;
                proxy_pass http://127.0.0.1:{4};
            }}
    }}'''.format(ssl_certificate,ssl_certificate_key,random_name,domain,docker_port)
    try:
        f = open(nginx_path,'a')
        f.write(server_config)
        print(bcolors.OKGREEN + "new challenge on domain {0}.{1} added with docker port {2}".format(random_name,domain,docker_port) + bcolors.ENDC)
    except Exception as e:
        print(str(e))

def get_hostname_port():
    pattern = re.compile("(?<=server_name )(\S+)(?=(;))|(?<=proxy_pass )(\S+)(?=(;))")

    for i, line in enumerate(open('/etc/nginx/sites-enabled/default')):
        for match in re.finditer(pattern, line):
            if '127.0.0.1' in match.group():

                print bcolors.WARNING + 'Docker Port %s' % (match.group()) + '\t' + bcolors.ENDC
            else:
                print bcolors.OKGREEN + 'Hostname is %s'%(match.group()) + bcolors.ENDC



if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("You need to run the following command")
        print(bcolors.FAIL + "python {0} /etc/letsencrypt/live/ctf.sherif.ninja/fullchain.pem /etc/letsencrypt/live/ctf.sherif.ninja/privkey.pem ctf.sherif.ninja 8443".format(sys.argv[0]) + bcolors.ENDC)
        get_hostname_port()
        exit(1)
    else:
        ssl_certificate = sys.argv[1]
        ssl_certificate_key = sys.argv[2]
        domain = sys.argv[3]
        docker_port = sys.argv[4]
        generate_challenges(ssl_certificate,ssl_certificate_key,domain,docker_port)
