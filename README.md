# OVH Email Redirection Management Tool

This script provides a command-line interface (CLI) to manage email redirections for OVH email domains.
The script interacts with the OVH API to `list`, `add` and `delete` information about email redirections.
Redirections are locally cached for quick lookup.

Features:
- `great`: Query OVH API and displays your firstname. This allows you to test your credentials setup.
- `list`: Fetch and display all redirections for a specified domain.
- `add`: Create a new redirection for an email address.
- `delete`: Delete a redirection by its ID.
- `info`: Get detailed information about a specific redirection.


## Table of contents

- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Usage](#usage)
- [Caching](#caching)


> [!NOTE]
> This code was written specifically to solve my unique requirements, use cases and workflows. It may not follow the most optimal practices or be universally applicable.
> 
> If you find the code useful for your purposes, feel free to use or modify it as needed. However, I cannot guarantee its suitability for any use case other than my own. Use at your own discretion! 😊


## Prerequisites

Before using `ovhdns-cli`, you will need:
- `python >= 3.x`


### Credentials

Head over to [https://api.ovh.com](https://api.ovh.com) to obtain the following API credentials from your OVH account:
- Application key
- Application secret
- Consumer key


### Dependencies

`ovhdns-cli` uses the following python packages:
- [click](https://pypi.org/project/click/)
- [more-itertools](https://pypi.org/project/more-itertools/)
- [ovh](https://pypi.org/project/ovh/)
- [tabulate](https://pypi.org/project/tabulate/)
- [tqdm](https://pypi.org/project/tqdm/)

`ovhdns-cli` runs well if you have [uv](https://docs.astral.sh/uv/) installed.


## Configuration

`ovhdns-cli` requires the following env variables to be set:

```Shell
export OVH_ENDPOINT=ovh-eu
export OVH_APPLICATION_KEY=OVH_APPLICATION_KEY
export OVH_APPLICATION_SECRET=OVH_APPLICATION_SECRET
export OVH_CONSUMER_KEY=OVH_CONSUMER_KEY
```

You also need a default `MAIL_PATTERN` env variable.

Redirecting to a gmail account:
```Shell
export MAIL_PATTERN=my_account+{}@gmail.com
```

Redirecting to a proton account:
```Shell
export MAIL_PATTERN=my_account+{}@protonmail.com
```


## Usage

Run the script by executing it directly `./ovhdns-cli.py`, or `uv run ovhdns-cli.py`:

```Shell
$ ./ovhdns-cli.py --help
Usage: ovhdns-cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add
  delete
  great
  info
  list
```


### Validate Setup

Validates your credentials by calling the OVH API.

```Shell
./ovhdns-cli.py great
```


### List Redirections

List and [cache](#caching) all redirections for a given domain:

```Shell
./ovhdns-cli.py list your_domain.com
```

This command takes an optional number of processes to use for parallel data fetching (default: 10).

```Shell
./ovhdns-cli.pyh list your_domain.com --processes 5
```


### Add Redirection

Add a new email redirection:

```Shell
./ovhdns-cli.py add redirection_name@your_domain.com
```

This command takes an optional argument `--localcopy` to keep a local copy of emails (default: `--no-localcopy`).

```Shell
./ovhdns-cli.py add redirection_name@your_domain.com --localcopy
```

This command takes an optional argument `--pattern` to override the MAIL_PATTERN environment variable.

```Shell
./ovhdns-cli.py add redirection_name@your_domain.com --pattern 'my_account+{}@another_mail_provider.com'
```


### Delete Redirection

Delete a redirection by its ID:

```Shell
./ovhdns-cli.py delete your_domain.com [ID]
```

> [!TIP]
> [ID] can be retrieved using the `list`command


### Retrieve Redirection Info

Retrieve information about a specific redirection:

```Shell
./ovhdns-cli.py info your_domain.com [ID]
```


## Caching

The script uses a local cache (stored in `./cache.json`) to store redirection data and optimize lookup.
Cached data is updated during the `list` command by syncing with the OVH API.
