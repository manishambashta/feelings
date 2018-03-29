from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

CONDITIONS = (

    (0, 'Ecstatic'),
    (20, 'Passionate'),
    (30, 'Happy'),
    (40, 'Optimistic'),
    (50, 'Content'),
    (60, 'Bored'),
    (62, 'Tired'),
    (65, 'Hungry'),
    (70, 'Pessimistic'),
    (80, 'Frustrated'),
    (90, 'Overwhelmed'),
    (100, 'Disappointed'),
    (110, 'Worried'),
    (120, 'Angry'),
    (130, 'Jealous'),
    (140, 'Insecure'),
    (150, 'Guilty'),
    (160, 'Fear'),
    (170, 'Grief'),
    (180, 'Despair'),
    (190, 'Paranoia'),

)


class Thought(models.Model):
    user = models.ForeignKey(User, related_name="thoughts", on_delete=models.CASCADE)
    recorded_at = models.DateTimeField(default=timezone.now, editable=False)
    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default="")

    def __str__(self):
        return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.get_condition_display())
