from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now

from apps.categories.models import Categories


class Todo(models.Model):
    users = models.ManyToManyField(User)
    categories = models.ForeignKey(Categories, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    text = models.TextField()

    done = models.BooleanField(default=False)
    done_at = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    days = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

