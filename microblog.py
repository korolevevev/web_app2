from app import app, db
from app.models import User, Post, PostLike
from app.commands import create_tables

if __name__ == '__main__':
    app.run(debug=False)

app.cli.add_command(create_tables)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}