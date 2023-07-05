from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Group)
admin.site.register(models.Question)
admin.site.register(models.Variant)
admin.site.register(models.UserAnswerGroup)
admin.site.register(models.UserAnAnswer)
