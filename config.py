import os

DB_PASSWORD = os.getenv('DB_PASSWORD', 'db_password')
SECRET_KEY = os.getenv('SECRET_KEY', 'key')
ALGORITHM = os.getenv('ALGORITHM', 'type')
ADMIN_NICKNAME = os.getenv('ADMIN_NICKNAME', 'nickname')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'password')
