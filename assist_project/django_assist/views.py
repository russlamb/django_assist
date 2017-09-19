from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Step, Command

class IndexView(generic.ListView):
    template_name = 'django_assist/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Step.objects.order_by('step_order')[:5]



class DetailView(generic.DetailView):
    model = Step
    template_name = 'django_assist/detail.html'

class ResultsView(generic.DetailView):
    model = Step
    template_name = 'django_assist/results.html'

def run_step(request, step_id):
    step = get_object_or_404(Step, pk=step_id)
    try:
        selected_command = step.choice_set.get(pk=request.POST['command'])
    except (KeyError, Command.DoesNotExist):
        # Redisplay the step run form.
        return render(request, 'django_assist/detail.html', {
            'step': step,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_command.output_text = ""
        selected_command.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('django_assist:results', args=(step.id,)))