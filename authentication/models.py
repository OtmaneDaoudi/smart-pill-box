from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoleBasedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isDoctor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.isDoctor} {self.user.username}"