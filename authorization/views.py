from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from . import forms


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = forms.UserCreation_Form
    success_url = reverse_lazy('firstpage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Сразу логиню пользователя
        return HttpResponseRedirect(self.success_url)
