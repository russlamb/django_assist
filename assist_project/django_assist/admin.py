from django.contrib import admin

from .models import Step, Command, StepStatus

def get_latest_step_order():
    return Step.objects.latest('step_order').step_order+1

class StepAdmin(admin.ModelAdmin):
    fields = ["step_name","step_status","step_order"]
    #prepopulated_fields = {'step_order': (get_latest_step_order(),)}
    ordering = ('step_order',)

    def view_step_order(self, obj):
        return obj.step_order


    view_step_order.empty_value_display = "???"


    def get_changeform_initial_data(self, request):
        return {
            'step_order': get_latest_step_order()
        }

admin.site.register(Step, StepAdmin)
admin.site.register(Command)
admin.site.register(StepStatus)
