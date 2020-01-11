from django.db import models

class Label(models.Model):
    name = models.TextField()
    headquarters = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Artist(models.Model):
    stage_name = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    year_of_birth = models.PositiveSmallIntegerField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.stage_name


class Song(models.Model):
    CHOICES = (
        ('r', 'Rock'),
        ('j', 'Jazz'),
        ('t', 'Techno'),
        ('k', 'Klassik')
    )

    title = models.TextField()
    genre = models.TextField(max_length=1, choices=CHOICES, null=True)
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)
    lyrics = models.TextField()
    artist = models.ManyToManyField('Artist', blank=True)

    def __str__(self):
        return self.title
