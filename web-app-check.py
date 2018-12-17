#!/usr/bin/python3.6
import subprocess
import argparse
ap = argparse.ArgumentParser(prog="WebSoftware Checker")
ap.add_argument("--url", "-u", help="List the WebSoftwares of your domain")
args = ap.parse_args()
host = args.url
http = 'http://'
trail = '/'
domain = http + host + trail
print("\n\n\n\t\t\tWEB APPLICATIONS DETECTED FOR",host.upper(),"\n\t\t\t","#"*37, "\n\n")
print(subprocess.call('/usr/bin/wad -u' +  domain, shell=True))