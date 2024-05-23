from django.views.generic import ListView, UpdateView
from .models import Issue, Status
from django.urls import reverse_lazy

class BoardView(ListView):
    template_name = 'issues/board.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name='to do')
        in_prog = Status.objects.get(name='in progress')
        done = Status.object.get(name='done')
        context['to_do_list'] = Issue.objects.filter(
            status=to_do
        ).order_by('created_on').reverse()
        context['in_prog_list'] = Issue.objects.filter(
            status=in_prog
        ).order_by('created_on').reverse()
        context['done_list'] = Issue.objects.filter(
            status=done
        ).order_by('created_on').reverse()
        return context
    
class StatusUpdateView(UpdateView):
    template_name = 'issues/edit.html'
    model = Issue
    fields = ['status']