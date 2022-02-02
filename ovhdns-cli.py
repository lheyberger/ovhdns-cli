#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ovh
from os import environ


OVH_ENDPOINT = environ.get('OVH_ENDPOINT')
OVH_APPLICATION_KEY = environ.get('OVH_APPLICATION_KEY')
OVH_APPLICATION_SECRET = environ.get('OVH_APPLICATION_SECRET')
OVH_CONSUMER_KEY = environ.get('OVH_CONSUMER_KEY')


def main():
    client = ovh.Client(
        endpoint=OVH_ENDPOINT,
        application_key=OVH_APPLICATION_KEY,
        application_secret=OVH_APPLICATION_SECRET,
        consumer_key=OVH_CONSUMER_KEY,
    )

    print('Welcome', client.get('/me')['firstname'])


if __name__ == '__main__':
    main()
