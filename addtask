#!/usr/bin/env python2

from apiclient.discovery import build
from argparse import ArgumentParser
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import run_flow
import httplib2

import parsedatetime
from datetime import date
import calendar
import os


CONFIG_DIR = os.path.join(os.environ['HOME'], '.config', 'addtask')
KEYS_FILE = os.path.join(CONFIG_DIR, 'keys.txt')
OAUTH_FILE = os.path.join(CONFIG_DIR, 'oauth.dat')


class Auth():
    def __init__(self, key_file):
        try:
            with open(key_file, 'r') as f:
                self.clientid = f.readline().strip()
                self.clientsecret = f.readline().strip()
                self.apikey = f.readline().strip()
        except IOError:
            self.clientid = raw_input("Enter your clientID: ")
            self.clientsecret = raw_input("Enter your client secret: ")
            self.apikey = raw_input("Enter your API key: ")
            self.write_auth()

    def write_auth(self):
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)
        with open(KEYS_FILE, 'w') as auth:
            auth.write(str(self.clientid) + '\n')
            auth.write(str(self.clientsecret) + '\n')
            auth.write(str(self.apikey) + '\n')


def add_task(service, title, due):
    try:
        ret = service.tasks().insert(tasklist="@default", body=dict(title=title, due=due)).execute()
        print ("Added task '{0}'".format(ret["title"]))
    except (EnvironmentError, TypeError) as e:
        print ("Error adding task: {0}".format(str(e)))


def make_parser():
    parser = ArgumentParser(description = """Add to Google Tasks with natural language""")

    parser.add_argument('strs', metavar='string', type=str, nargs='*',
        help='Can be something like "Pick up milk today"')

    key_exist = os.path.exists(KEYS_FILE)
    auth_exist = os.path.exists(OAUTH_FILE)

    if not key_exist or not auth_exist:
        # Required by oauth2client
        parser.add_argument('--auth_host_name', default='localhost',
                       help='Hostname when running a local web server.')
        parser.add_argument('--noauth_local_webserver', action='store_true',
                       default=False, help='Do not run a local web server.')
        parser.add_argument('--auth_host_port', default=[8080, 8090], type=int,
                       nargs='*', help='Port web server should listen on.')
        parser.add_argument('--logging_level', default='ERROR',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                       help='Set the logging level of detail.')
    return parser


def authenticate(args):
    f = Auth(KEYS_FILE)

    storage = Storage(OAUTH_FILE)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        # OAuth 2.0 Authentication
        FLOW = OAuth2WebServerFlow(
            client_id=f.clientid,
            client_secret=f.clientsecret,
            scope='https://www.googleapis.com/auth/tasks',
            user_agent='Tasky/v1')

        credentials = run_flow(FLOW, storage, args)

    http = httplib2.Http()
    http = credentials.authorize(http)

    # The main Tasks API object
    return build(serviceName='tasks', version='v1', http=http, developerKey=f.apikey)


def parse(args):
    command = " ".join(args.strs)
    cal = parsedatetime.Calendar()
    datetime, kind = cal.parse(command)
    dt = date.fromtimestamp(calendar.timegm(datetime))

    if not kind:
        print ("Couldn't parse out a date, using today")
    else:
        print ("Parsed date: {0}".format(dt.strftime("%a %b %d %Y")))

    return command, dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def main(service, args):

    if len(args.strs) < 1:
        args.print_help()
        return

    title, date = parse(args)
    add_task(service, title, date)


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    service = authenticate(args)
    if len(args.strs) <1:
        parser.print_help()
    else:
        main(service, args)
