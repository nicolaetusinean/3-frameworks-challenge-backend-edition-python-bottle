from jwcrypto import jwt, jwk
from bottle import request, response
from models.user import User
from config import keyToSignCookie


class AuthController:
    def __init__(self):
        self.key = {"k": "7vE-VipgZhCWpzyZASwO5r_4RauQrIuEXiYTRSN0WDk", "kty": "oct"}

    def create_jwt_token(self):
        key = jwk.JWK(**self.key)
        # TODO: add expire date
        token = jwt.JWT(header={"alg": "HS256"}, claims={"info": "I'm a signed token"})
        token.make_signed_token(key)
        token.serialize()

        encrypted_token = jwt.JWT(header={"alg": "A256KW", "enc": "A256CBC-HS512"}, claims=token.serialize())
        encrypted_token.make_encrypted_token(key)
        encrypted_token.serialize()

        return encrypted_token

    def decrypt_jwt_token(self, encrypted_token):
        key = jwk.JWK(**self.key)
        enc_token = jwt.JWT(key=key, jwt=encrypted_token)
        standard_token = jwt.JWT(key=key, jwt=enc_token.claims)

        return standard_token

    def login(self, db):
        try:
            token = self.create_jwt_token()

            body = request.json

            username = body["username"]
            password = body["password"]

            if self.find_user(db, username, password):
                response.set_cookie("token", token.serialize(), secret=keyToSignCookie, path='/', httponly=True)

                return {
                    "success": True,
                    "username": username
                }
        except Exception, e:
            return {"error": "Some error has occurred. " + str(e)}

    def logout(self):
        response.delete_cookie("token")

    def find_user(self, db, username, password):
        user = db.query(User).filter_by(username=username).first()

        # TODO: use password encryption
        if user and user.password == password:
            return True

        return False
