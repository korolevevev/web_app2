from app import app, db
from app.models import User, Post
import click
from flask.cli import with_appcontext

if __name__ == '__main__':
    app.run(debug=False)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()