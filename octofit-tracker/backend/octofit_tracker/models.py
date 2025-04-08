from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.description}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return self.name
