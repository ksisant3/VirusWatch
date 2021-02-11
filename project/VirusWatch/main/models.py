from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'files/user_{0}/{1}'.format(instance.user.id, filename)

class File(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    file = models.FileField(upload_to = user_directory_path)

    def __str__(self):
        return self.name
