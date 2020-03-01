from controllers.hello import HelloController
from controllers.auth import AuthController


def setup_routing(app):
    hello_controller = HelloController()
    auth_controller = AuthController()

    app.route('/hello/authenticated/<name>', callback=hello_controller.authenticated_only)
    app.route('/hello/<name>', callback=hello_controller.hello)
    app.route('/auth/login', 'POST', auth_controller.login)
    app.route('/auth/logout', 'DELETE', auth_controller.logout())
