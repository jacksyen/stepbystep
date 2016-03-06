import urllib

public_ip = "None"
target_url = 'http://ip.42.pl/raw'

## todo change to requests
def get_public_ip(request_target):
    with urllib.request.urlopen('http://python.org/') as response:
        public_ip_address = response.read()
    return public_ip_address

public_ip=get_public_ip(target_url)
if "None" not in public_ip:
    print("Your Public IP address is: %s") % (str(public_ip))
else:
    print("Your Public IP address was not found")
