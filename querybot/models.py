"""Models for querybot."""
from uuid import uuid4
from django.db import models

class Query(models.Model):
    """A single entry on the FAQ Page."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    category = models.CharField(max_length=30, blank=False)
    sub_category = models.CharField(max_length=30, blank=True)
    sub_sub_category = models.CharField(max_length=30, blank=True)

class UnresolvedQuery(models.Model):
    """New question asked by someone."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question = models.TextField(blank=False)
    category = models.CharField(max_length=30, blank=True)
