from django.views import View
from django.shortcuts import render, redirect
from pratice2 import models, forms
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse

import datetime


# вьюхи == контроллеры == обработчики запросов == представления??????

# воемя через функцию
def example_view_function(request):
    html = "Okay, it's {} now.".format(datetime.datetime.now())
    # template_name = 'time.html'
    return HttpResponse(html)


# время через темплейт
class example_view_template(View):
    def get(self, request):
        return render(request, 'time.html', {'time': datetime.datetime.now()})


# по айди вывести инфу о car owner
class OwnerView(View):
    def get(self, request, pk):
        # исключение если айди клиента нет
        # без исключения - крашится. в дженерике автоматом
        # дается 404 (в отличие от данного подхода, если не прописать блок try-except)
        try:
            owner = models.Owner.objects.get(pk=pk)
        except models.Owner.DoesNotExist:
            raise Http404("Owner with required ID does not exist")

        # ключ - имя объекта переданного из контроллера
        # по которому обращаемся к объекту owner в owner.html
        return render(request, 'owner.html', {'object': owner})


class OwnerViewGeneric(DetailView):
    model = models.Owner
    # в дженерике обращаемся к объекту в owner.html как к object(!!!!)
    template_name = 'owner.html'


class OwnerViewList(ListView):
    model = models.Owner
    template_name = 'owner_list.html'


class OwnerForm(View):
    form_class = forms.OwnerCreationForm


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, 'userowner_form.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.OwnerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(user.get_absolute_url())
        context = {'form': form}
        return render(request, 'userowner_form.html', context)



class CarView(DetailView):
    model = models.Car
    template_name = 'car_detail.html'

class CarCreateView(CreateView):
    model = models.Car
    template_name = 'car_form.html'
    fields = [
        'license_plate',
        'brand',
        'model'
    ]

#
class CarUpdateView(UpdateView):
    model = models.Car
    template_name = 'car_form.html'
    fields = [
        'license_plate',
        'brand',
        'model'
    ]


class CarDeleteView(DeleteView):
    model = models.Car
    template_name = 'car_form.html'
    success_url = reverse_lazy('pratice2:OwnerList')
