# coding:utf-8


from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# 创建flask的应用对象
app = create_app("develop")

# python manage.py runserver 127.0.0.1:5000
manager = Manager(app)

#
Migrate(app, db)

# python manage.py db init
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
