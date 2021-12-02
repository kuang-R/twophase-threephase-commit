from django.db import models

# Create your models here.
class TwoPhaseParticipant(models.Model):
    name = models.CharField(max_length=64)
    state = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class TwoPhaseValue(models.Model):
    participant = models.ForeignKey(TwoPhaseParticipant, on_delete=models.CASCADE)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    prepared_value = models.CharField(max_length=64)
    def __str__(self):
        return participant.name + ':' + self.key + ' ' + self.value
