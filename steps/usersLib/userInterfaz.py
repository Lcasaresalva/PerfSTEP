from locust import HttpUser


'''Esta clase se usará como interfaz para los usuarios de cualquier tipo que accedan a la app'''


class UserInterfaz(HttpUser):
   # host = "https://reqres.in"

    abstract: bool = True

    def __init__(self, parent):
        super(UserInterfaz, self).__init__(parent)
        self.user_attr = {}
        # todos los atributos que yo quiera de httpuser

    def set_userId(self, userId):
        self.user_attr['userId'] = userId

    def get_userIdl(self):
        if 'userId' in self.user_attr:
            return self.user_attr['userId']
        else:
            return None

    def set_token(self, token):
        self.user_attr['token'] = token
        return self

    def get_token(self):
        if 'token' in self.user_attr:
            return self.user_attr['token']
        else:
            return None
