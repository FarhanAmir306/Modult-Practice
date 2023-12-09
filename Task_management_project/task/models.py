from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=200)
    taskDescription =models.TextField()
    is_completed =models.BooleanField(default=False)
    Task_Assign_Date=models.DateTimeField()
    task=models.ManyToManyField(CategoryModel)

    def __str__(self) -> str:
        return self.taskTitle

