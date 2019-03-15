from django.db import models

class Thing(models.Model):
    name = models.TextField()
    date = models.DateField()
    points = models.IntegerField()
    content = models.TextField()
    reporting_date = models.DateTimeField()
    class Meta:
        managed = True
        db_table = 'things'

class Request(models.Model):
    name = models.TextField()
    reporting_date = models.DateTimeField()
    content = models.TextField()
    class Meta:
        managed = True
        db_table = 'requests'

class Chat(models.Model):
    name = models.TextField()
    reporting_date = models.DateTimeField()
    content = models.TextField()
    class Meta:
        managed = True
        db_table = 'chats'

class Tackle(models.Model):
    thing_id = models.ForeignKey(Thing, on_delete = models.CASCADE)
    reporting_date = models.DateTimeField()
    content = models.TextField()
    class Meta:
        managed = True
        db_table = 'tackles'
