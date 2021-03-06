#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from app import create_app, db
from app.models import *
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


def make_shell_context():
    return dict(app=app, db=db, SMS_Receive=SMS_Receive, TokenList=TokenList, BlackList=blacklist, Article=Article)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()
