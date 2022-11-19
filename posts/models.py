from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
