from django.db import models

class ModelA(models.Model):
    pass


class ModelB(models.Model):
    a_ptr = models.ForeignKey(ModelA, on_delete=models.CASCADE)
    x = models.IntegerField()

    class Meta:
        constraints = [
#            models.UniqueConstraint(fields=['a_ptr', 'x'], name='%(app_label)s_%(class)s_unique_a_ptr_x'),
        ]
