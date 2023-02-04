from django.db import models

class TodoListItem(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.content}"

    def __repr__(self):
        return f"{self.pk} - {self.content}"


    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

