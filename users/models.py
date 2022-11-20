from django.db import models
import uuid



class create(models.Model):
    student_division= models.CharField(max_length=255)
    student_class = models.CharField(max_length=255)

    def __str__(self):
        return self.student_class


class ToDo(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)/
    username = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    creat_task = models.CharField(null=False, blank=False, max_length=120)
    completed_task =models.BooleanField(default=False)


    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'

    def __str__(self):
        return self.creat_task

