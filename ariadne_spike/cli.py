from __future__ import print_function
import os

from ariadne.asgi import GraphQL
import click
import uvicorn

from ariadne_spike import query
from ariadne_spike import flask_server


@click.group()
def cli():
    pass


@click.command('webapp_asgi')
def webapp_asgi():
    app = build_webapp()
    port = int(os.getenv('PORT', '8000'))
    uvicorn.run(app, host="0.0.0.0", port=port)

@click.command('webapp_wsgi')
def webapp_wsgi():
    port = int(os.getenv('PORT', '8000'))
    flask_server.app.run(host='0.0.0.0', port=port, debug=True)

def build_webapp():

    schema = query.schema()
    return GraphQL(schema)


cli.add_command(webapp_asgi)
cli.add_command(webapp_wsgi)


if __name__ == '__main__':
    cli()
