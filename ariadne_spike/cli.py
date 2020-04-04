from __future__ import print_function

import click
import os
import uvicorn
from ariadne.asgi import GraphQL

from ariadne_spike import query


@click.group()
def cli():
    pass


@click.command('webapp')
def webapp():
    app = build_webapp()
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


def build_webapp():

    schema = query.schema()
    return GraphQL(schema)


cli.add_command(webapp)


if __name__ == '__main__':
    cli()
