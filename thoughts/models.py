from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

CONDITIONS=(

    (1, 'Ecstatic'),
    (2, 'Passionate'),
    (3, 'Happy'),
    (4, 'Optimistic'),
    (5, 'Content'),
    (6, 'Bored'),
    (7, 'Pessimistic'),
    (8, 'Frustrated'),
    (9, 'Overwhelmed'),
    (10, 'Disappointed'),
    (11, 'Worried'),
    (12, 'Angry'),
    (13, 'Jealous'),
    (14, 'Insecure'),
    (15, 'Guilty'),
    (16, 'Fear'),
    (17, 'Grief'),
    (18, 'Despiar'),

)


class Thought(models.Model):
    user = models.ForeignKey(User, related_name="thoughts")
    recorded_at = models.DateTimeField(default=timezone.now, editable=False)
    conditions = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default="")