from django.db import models

# Create your models here.
class ModelFAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()
    eywords=models.JSONField(default=list)

    def __str__(self):
        return self.question    