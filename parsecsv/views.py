from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.hashers import check_password
from . import models


# Тест для конкретного пользователя
test_func = lambda self: self.request.user.username == 'uaenergy' and \
                         check_password('1qaz2wsx3edc', self.request.user.password)


# Выбираю куда перенаправить пользователя
def get_login_url(self):
    if self.request.user.is_authenticated:
        login_url = reverse_lazy('logout')
        self.redirect_field_name = None
    else:
        login_url = reverse_lazy('login')
    return login_url


# Убрал появление исключения если user.is_authenticated. Что бы перенаправлять залогиненого пользователя на logout
def handle_no_permission(self):
    from django.core.exceptions import PermissionDenied
    from django.contrib.auth.views import redirect_to_login

    if self.raise_exception:
        raise PermissionDenied(self.get_permission_denied_message())
    return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


class FirstPage(UserPassesTestMixin, CreateView):
    template_name = 'parsecsv/1.html'
    model = models.CSVFile
    fields = ['file']
    success_url = reverse_lazy('secondpage')
    test_func = test_func
    get_login_url = get_login_url
    handle_no_permission = handle_no_permission


class SecondPage(UserPassesTestMixin, TemplateView):
    template_name = 'parsecsv/2.html'
    test_func = test_func
    get_login_url = get_login_url
    handle_no_permission = handle_no_permission

    def get_context_data(self, **kwargs):
        from random import choice
        from string import ascii_letters, digits

        context = super().get_context_data(**kwargs)
        # Создаю 1 таблицу
        varA = models.ParsedCSV.objects.get(string__startswith='Alpha A').string
        varA = varA.split(',')
        varA.pop(0)
        for i in range(len(varA)):
            if varA[i] == '0':
                varA[i] = '9'
        context['table1'] = varA

        # Создаю 2 таблицу
        varB = models.ParsedCSV.objects.get(string__startswith='Alpha B').string
        varB = varB.split(',')
        varB.pop(0)
        for i in range(len(varB)):
            if not((65 <= ord(varB[i]) <= 90) or (97 <= ord(varB[i]) <= 122)):
                varB[i] = None
        context['table2'] = varB

        # Создаю 3 таблицу
        table3 = []
        while len(table3) != 16:
            i = choice(ascii_letters + digits)
            if i not in table3:
                table3.append(i)
        context['table3'] = table3
        return context
