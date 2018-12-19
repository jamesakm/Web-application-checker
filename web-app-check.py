
#!/usr/bin/python3.6
import subprocess
import argparse

# Fun to check the applications
def web_app_check(domain):
  print(subprocess.call('/usr/bin/wad -u' +  domain, shell=True))
  return

ap = argparse.ArgumentParser(prog="WebSoftware Checker")
ap.add_argument("--url", "-u", help="List the WebSoftwares of your domain")
args = ap.parse_args()
host = args.url
http = 'http://'
trail = '/'
if host.startswith('http'):
 web_app_check(host)
else:
 domain = http + host + trail
 web_app_check(domain)
