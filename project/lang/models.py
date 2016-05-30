from __future__ import unicode_literals

from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=256)


class CodeSnippet(models.Model):
    code = models.TextField()
    language = models.ForeignKey(Language)
