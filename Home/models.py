from django.db import models

# Create your models here.
LANGUAGE_CHOICES=(('c','C'),('c++','C++'),('java','Java'),('python','Python'),('js','JavaScript'),('sql','SQL'))
class Share(models.Model):
    program=models.TextField()
    language=models.CharField(max_length=122, choices=LANGUAGE_CHOICES, default='c')
    code=models.TextField()
