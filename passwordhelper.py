import hashlib
import os
import base64

class PasswordHelper:
    
    def get_hash(self, plain):
        return hashlib.sha256(str(plain).encode('utf-8')).hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20))
    
    def validate_password(self, plain, salt, expected):
        return self.get_hash(str(plain)+str(salt)) == expected