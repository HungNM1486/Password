from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    encrypted_password = models.BinaryField()  # Mật khẩu đã mã hóa
    created_at = models.DateTimeField(auto_now_add=True)

    # Phương thức mã hóa mật khẩu
    def set_password(self, raw_password):
        cipher_suite = Fernet(settings.ENCRYPTION_KEY)
        self.encrypted_password = cipher_suite.encrypt(raw_password.encode())

    # Phương thức giải mã mật khẩu
    def get_password(self):
        cipher_suite = Fernet(settings.ENCRYPTION_KEY)
        return cipher_suite.decrypt(self.encrypted_password).decode()
    