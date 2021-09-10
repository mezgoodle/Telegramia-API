from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    @staticmethod
    def bcrypt(password: str):
        hashed_password = pwd_context.hash(password)
        return hashed_password
