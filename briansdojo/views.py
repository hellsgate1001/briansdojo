from django.core.urlresolvers import reverse
from django.views.generic import FormView

from .forms import ContactForm
from .models import Project


class HomeView(FormView):
    template_name = 'home.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        self.request.session['contact_success'] = True
        return super(HomeView, self).form_valid(form)

    def form_invalid(self, form):
        for name, field in form.fields.items():
            if form.errors.get(name, None):
                form.fields[name].widget.attrs['placeholder'] += ': %s' % '; '.join(form.errors[name])
                form.fields[name].widget.attrs['class'] = 'error'

        return super(HomeView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        if self.request.session.get('contact_success', None):
            context['contact_success'] = True
            del(self.request.session['contact_success'])
        return context
