from models.user import User


def seed_db(app):
    sqlalchemy = None
    for plugin in app.plugins:
        if plugin.name == "sqlalchemy":
            sqlalchemy = plugin
            break

    if not sqlalchemy:
        return False

    print "add users to DB"
    user1 = User("nicu", "pass")
    session = sqlalchemy.create_session(bind=sqlalchemy.engine)
    session.add(user1)
    session.commit()
    print "done"

    return True