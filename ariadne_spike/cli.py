#!/usr/bin/python
# coding=utf-8

from __future__ import print_function

import click


@click.group()
def cli():
    pass


@click.command('command1')
@click.option('--name')
def command1(name):
    print(name)


cli.add_command(command1)

if __name__ == '__main__':
    cli()
