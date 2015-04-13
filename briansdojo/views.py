from django.views.generic import TemplateView

from .models import Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
