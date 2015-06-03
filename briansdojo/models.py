from django.db import models

from sorl.thumbnail import ImageField


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(max_length=255)
    image = ImageField(upload_to='briansdojo/project/', max_length=255)

    def __unicode__(self):
        return self.title


class Contact(models.Model):
    sender = models.CharField("Name", max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{sender}: {sent}'.format(
            sender=self.sender,
            sent=self.sent.strftime('%Y-%m-%d %H:%M:%S')
        )
