from __future__ import print_function

import click
import uvicorn
from ariadne.asgi import GraphQL

from ariadne_spike import query


@click.group()
def cli():
    pass


@click.command('webapp')
def webapp():
    app = build_webapp()
    uvicorn.run(app, debug=True)


def build_webapp():
    schema = query.schema()
    return GraphQL(schema, debug=True)


cli.add_command(webapp)


if __name__ == '__main__':
    cli()
