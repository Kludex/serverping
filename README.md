# Server Ping

A FastAPI application that pings a server from time to time to know its status.

## Installation

We're using [poetry](https://python-poetry.org/) as package manager, so in case you don't have it:

``` bash
pip install poetry
```

As for the dependencies, you just need to:

``` bash
poetry install
```

## Usage

The usage is pretty simple. But I'll give the complete information you need to do it.

First of all, you'll need an `.env` file, so I recommend you to copy the `env.example` and change its name.

### Variables

The variables you need are:

* `SLACK_API_TOKEN` : The slack API token that you can get from your [slack app environment](https://api.slack.com/apps/).
* `CHANNEL_ID` : You can get it from web slack, as the channels always have the same format: `app.slack.com/client/<SERVER_ID>/<CHANNEL_ID>` .
* `HOST` : Server host.
* `PORT` : Server port.
* `SERVER_NAME` : The server name, doesn't need to be the real one.
* `PING_TIME` : Time interval on which you'll ping the server.

### Run the server

Uvicorn is all we need.

``` bash
uvicorn serverping:app
```

You can pass [additional parameters](https://www.uvicorn.org/settings/) to `uvicorn` if you want, but the above command should be enough.

## License

This project is licensed under the terms of the MIT license.
