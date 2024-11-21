from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(default='')

    def __str__(self):
        return f"{self.id} {self.username}"

class Groups(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.id} {self.name}"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    subject = models.CharField(max_length=50)
    subtopic = models.TextField()

    def __str__(self):
        return f"{self.id} {self.subject} {self.subtopic}"

class Appointments(models.Model):
    subject = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    color = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    notes = models.TextField()
    isAllDay = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Groups, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} de {self.user.username} : {self.subject}"