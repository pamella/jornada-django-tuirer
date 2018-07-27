from django.db import models


# adição dessa função na classe objects default do django
# https://docs.djangoproject.com/en/1.7/ref/models/queries/
class TuitesManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(content__icontains=query) |
            models.Q(author__username__icontains=query)
        )