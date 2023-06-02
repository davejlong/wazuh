import json
import sys
import time
import os

try:
    import requests
    from requests.auth import HTTPBasicAuth
except Exception as e:
    print("No module 'requests' found. Install: pip install requests")
    sys.exit(1)

debug_enabled = True
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_file = '{0}/logs/integrations.log'.format(pwd)

def debug(msg):
    if debug_enabled:
        msg = "{0}: {1}\n".format(now, msg)
        print(msg)
        f = open(log_file, "a")
        f.write(msg)
        f.close()


class Syncro:
    def __init__(self, api_key, hostname):
        self.api_key = apikey
        self.base_uri = "https://{0}.syncromsp.com/api/v1".format(hostname)
        self.debug_enabled = debug
        self.log_file = log_file
    
    def headers():
        return {
            'accept': 'application/json',
            'Authorization': self.api_key
        }

# All message_for_* methods should return a tuple (system name, message)
def message_for_office365(alert_json):
    tenant_id = alert_json['data']['office365']['OrganizationIdd']

def message_for_vulnerability(alert_json):
    agent_name = alert_json['agent']['name']

def message_for_firewall(alert_json):

def message_for_sca(alert_json):

def message_for_generic(alert_json):
    agent_name = alert_json['agent']['name']

def main(args):
    # Grab everything from the arguments passed in
    api_key = args[2]
    api_host = args[3]

    # Get an instance of the Syncro class
    s = Syncro(api_key, api_host)

    # Start parsing the alert
    alert_file = open(args[1])
    alert_json = json.loads(alert_file.read())
    alert_file.close()

    match alert_json['location']:
        case 'office365':
        case 'vulnerability-detector':

        case '/var/log/syslog-ng/messages':

        case 'sca':

        case _:

    debug(alert_json)



if __name__ == "__main__":
    main(sys.argv)