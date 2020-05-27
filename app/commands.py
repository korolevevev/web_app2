import click
from flask.cli import with_appcontext

from .__init__ import app, db
from app.models import User, Post, PostLike

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()