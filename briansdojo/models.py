from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='briansdojo/project/', max_length=255)

    def __unicode__(self):
        return self.title

    def save(self):
        '''
        Validate we have an image as the ImageField value
        '''
        import pdb;pdb.set_trace()


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
