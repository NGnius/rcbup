'''
Created by NGnius 2019-06-17
'''
import argparse
import time
import json
from os import makedirs
from os.path import join
from rcapi import auth, factory

SLOWDOWN = 0.5  # prevent more than two requests per second
CALLS_BEFORE_REFRESH = 4  # token expires every 60s or something

def main(args):
    token = ''
    credentials = do_login(args)
    if credentials is None:
        return
    token = credentials['Token']
    makedirs(args.out, exist_ok=True)
    search_params = factory.make_search_body(search=args.search, player=args.player)
    robots = factory.factory_list(token, search_params)

    calls = 0
    for bot in robots:
        if calls % CALLS_BEFORE_REFRESH == 0 and args.batch:
            print('Refreshing token...')
            token = do_login(args)['Token']
        save_path = join(args.out, bot['itemName']+'.'+args.extension.lstrip('.'))
        print('Downloading %s to %s...' % (bot['itemName'], save_path))
        bot_info = factory.factory_bot(token, robots[0]['itemId'])
        with open(save_path, 'w') as f:
            json.dump(bot_info, f, indent=4)
        if calls == args.max and args.max >= 0:
            return
        calls += 1
        if args.batch:
            time.sleep(SLOWDOWN)

def do_login(args):
    if args.password is None and args.username is None:
        return auth.fj_login()
    elif args.password is not None and args.username is not None:
        return auth.fj_login(username = args.u, password=args.p)
    else:
        print('! Password and username must both be present or both missing.')
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--password', '-p', metavar='PASSWORD', type=str,
                        default=None, help='Your password to login to Robocraft')
    parser.add_argument('--username', '-u', metavar='USERNAME', type=str,
                        default=None, help='Your username to login to Robocraft')
    parser.add_argument('--search', metavar='TEXT', type=str,
                        default='', help='The search text')
    parser.add_argument('--out', '-o' , metavar='PATH', type=str,
                        default='./', help='Output folder path')
    parser.add_argument('--batch', '-l', action='store_true',
                        default=False, help='Handle chores for longer time periods')
    parser.add_argument('--player', action='store_true',
                        default=None, help='Search players only')
    parser.add_argument('--extension', metavar='EXT', type=str,
                        default='bot', help='File extension to use to store the plaintext files')
    parser.add_argument('--max', metavar='N', type=int,
                        default=-1, help='Maximum bots to download')

    args = parser.parse_args()

    main(args)
    print('Done.')