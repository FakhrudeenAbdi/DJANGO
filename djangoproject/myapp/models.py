from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(Editor, on_delete=models.SET_NULL, null=True, related_name='posts')

    def __str__(self):
        return self.title

