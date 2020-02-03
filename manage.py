#!/usr/bin/env python
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from flask_script import Manager, Shell

from models import Yeshuv

app = create_app('default')
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
 """Run the unit tests."""
 import unittest
 tests = unittest.TestLoader().discover('tests')
 unittest.TextTestRunner(verbosity=2).run(tests)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Yeshuv=Yeshuv, app=app, ) #, User=User, Follow=Follow, Role=Role, Permission=Permission)

manager.add_command("shell", Shell(make_context=make_shell_context))


def userDB():
    pass


if __name__ == '__main__':
    manager.run()

