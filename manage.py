from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash

from webapp import create_app, db
from webapp.models import User


app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def create_user():
    db.session.add(User(
        email=input("Admin email: "),
        password=generate_password_hash(input("Admin password: "), method='sha256'))
    )
    db.session.commit()


@manager.command
def drop_db():
    db.drop_all()


@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
