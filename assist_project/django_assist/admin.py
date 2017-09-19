from django.contrib import admin

from .models import Step, Command, StepStatus


admin.site.register(Step)
admin.site.register(Command)
admin.site.register(StepStatus)