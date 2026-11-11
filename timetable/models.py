

# Create your modelsfrom django.db import models

from django.db import models

class TimeSlot(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    subject = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100, default="")
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.day} {self.start_time}-{self.end_time} {self.subject}"