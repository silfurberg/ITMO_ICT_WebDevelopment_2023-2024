# views
```python
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from itertools import groupby
from collections import OrderedDict, defaultdict
from django.db.models import QuerySet, F
from django.conf import settings

from homework import forms, models

class RootPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'homework/root_page.html', {'name': request.user.username})
        return render(request, 'homework/root_page.html')


class LoginView(View):
    def get(self, request):
        form = forms.UserLoginForm()
        return render(request, 'homework/login.html', {'form': form})

    def post(self, request):
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('homework:root'))
            else:
                messages.error(request, 'Неверный логин или пароль')
        return render(request, 'homework/login.html', {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('homework:root'))


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegisterForm()
        context = {'form': form}
        return render(request, 'homework/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        context = {'form': form}
        return render(request, 'homework/registration.html', context)


class HomeworksView(LoginRequiredMixin, ListView):
    model = models.Homework
    template_name = 'homework/homeworks.html'

    def get_queryset(self):
        user = self.request.user
        assigned_homeworks_qs = user.assigned_homeworks.get_queryset()
        return assigned_homeworks_qs


class SubmitHomeworkView(LoginRequiredMixin, UpdateView):
    model = models.StudentHomework
    fields = ['answer']
    success_url = reverse_lazy('homework:homeworks')


class GradesView(View):

    def get(self, request):
        # get subjects and usernames and sort them
        subjects = list(models.Subject.objects.all().values_list('title', flat=True))
        subjects.sort()
        usernames = list(models.Student.objects.all().values_list('username', flat=True))
        usernames.sort()
        # prepare ordered dict to be filled with marks
        subject_username_grades = OrderedDict()
        for subject in subjects:
            subject_username_grades[subject] = {}
            for username in usernames:
                subject_username_grades[subject][username] = []
        # filter queryset
        homeworks = models.StudentHomework.objects.filter(mark__isnull=False)
        # annotate queryset with subject_title and username
        annotated_homeworks = homeworks.annotate(
            subject_title=F('homework__subject__title'),
            username=F('student__username')
        ).values(
            'subject_title', 'username', 'mark'
        )

        # Populate add marks to OrderedDict
        for hw in annotated_homeworks:
            subject = hw['subject_title']
            username = hw['username']
            mark = hw['mark']
            subject_username_grades[subject][username].append(mark)
        return render(request, 'homework/marks.html', {'subject_username_grades': subject_username_grades})
```