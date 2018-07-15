import falcon

from todoapi.models import User


class Resource:
    """
    REST API handlets for test
    """

    def on_post(self, req, resp):
        user = User()
        user['username'] = self._validate_username(req.get_json('username', dtype=str))
        user['email'] = self._validate_email(req.get_json('email', dtype=str))
        user['first_name'] = req.get_json('first_name', default=None, dtype=str)
        user['last_name'] = req.get_json('last_name', default=None, dtype=str)

        user.set_password(req.get_json('password', dtype=str))
        user.save()
        resp.json = {
            'msg': 'OK',
            'description': f"User '{user.username}' create!"
        }

    @staticmethod
    def _validate_username(username):
        user = User.objects(username=username).first()
        if user is not None:
            raise falcon.HTTPUnauthorized(
                title='409 Conflict',
                description='Username already exists',
                challenges=None).to_json()
        return username

    @staticmethod
    def _validate_email(email):
        user = User.objects(email=email).first()
        if user is not None:
            raise falcon.HTTPConflict(
                title='409 Conflict',
                description='Email already exists',
                challenges=None).to_json()
        return email
