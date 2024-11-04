#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ovh
import json
import click
import operator
from os import environ
from tqdm import tqdm
from itertools import repeat
from tabulate import tabulate
from multiprocessing import Pool
from pprint import pprint


OVH_ENDPOINT = environ.get('OVH_ENDPOINT', '')
OVH_APPLICATION_KEY = environ.get('OVH_APPLICATION_KEY', '')
OVH_APPLICATION_SECRET = environ.get('OVH_APPLICATION_SECRET', '')
OVH_CONSUMER_KEY = environ.get('OVH_CONSUMER_KEY', '')
MAIL_PATTERN = environ.get('MAIL_PATTERN', '')


client = ovh.Client(
    endpoint=OVH_ENDPOINT,
    application_key=OVH_APPLICATION_KEY,
    application_secret=OVH_APPLICATION_SECRET,
    consumer_key=OVH_CONSUMER_KEY,
)


def get_redirection_infos(redirection):
    domain, redirection_id = redirection
    try:
        return client.get(f"/email/domain/{domain}/redirection/{redirection_id}")
    except:
        return {
            'id': redirection_id,
            'from': '❌',
            'to': '❌',
        }


def display_results(redirections):
    redirections = ((r['id'], r['from'], r['to']) for r in redirections)
    redirections = sorted(redirections, key=operator.itemgetter(1))
    print(tabulate(redirections, headers=('ID', 'From', 'To')))


@click.group()
def main():
    pass


@main.command()
def great():
    print('Welcome', client.get('/me')['firstname'])


@main.command()
@click.argument('domain')
@click.option('--processes', default=10, help='Number of processes')
@click.option('--limit', default=5000, help='Limits the number of redirections')
def list(domain, processes, limit):
    redirections = client.get(f"/email/domain/{domain}/redirection")
    redirections = redirections[:limit]
    total = len(redirections)

    redirections = zip(repeat(domain), redirections)

    results = []
    with Pool(processes=processes) as pool:
        for result in tqdm(pool.imap_unordered(get_redirection_infos, redirections), total=total):
            results.append(result)
        pool.close()
        pool.join()

    display_results(results)


@main.command()
@click.argument('address')
@click.option('--localcopy/--no-localcopy', default=False, help='Keep local copy')
@click.option('--pattern', default=MAIL_PATTERN, type=str)
def add(address, localcopy, pattern):
    subdomain, domain = address.split('@')
    redirection = pattern.format(''.join(filter(str.isalnum, subdomain)))
    result = client.post(f"/email/domain/{domain}/redirection",
        _from=address,
        to=redirection,
        localCopy=localcopy,
    )
    print(json.dumps(result, indent=4))


@main.command()
@click.argument('domain')
@click.argument('id')
def delete(domain, id):
    result = client.delete(f"/email/domain/{domain}/redirection/{id}")
    print(json.dumps(result, indent=4))


@main.command()
@click.argument('domain')
@click.argument('id')
def info(domain, id):
    result = client.get(f"/email/domain/{domain}/redirection/{id}")
    print(json.dumps(result, indent=4))


if __name__ == '__main__':
    main()
