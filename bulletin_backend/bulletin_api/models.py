from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Bulletin(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk is None:  
            max_position = Bulletin.objects.aggregate(models.Max('position'))['position__max']
            if max_position is None:  
                self.position = 1
            else:
                self.position = max_position + 1
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=Bulletin)
def update_bulletin_position_on_delete(sender, instance, **kwargs):
    Bulletin.objects.filter(position__gt=instance.position).update(position=models.F('position') - 1)
