from bottle import request
from config import keyToSignCookie


class HelloController:
    def __init__(self):
        pass

    def hello(self, name='Stranger'):
        return {"id": 1, "name": name}

    def authenticated_only(self, name='Stranger'):
        try:
            token = request.get_cookie("token", secret=keyToSignCookie)
            if not token:
                raise Exception("Unauthenticated.")

            return {"id": 1, "name": name, "authenticated": True}

        except Exception, e:
            return {"error": "An error has occurred: " + str(e)}
