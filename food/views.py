from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.template import loader


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    # return HttpResponse(template.render(context, request))

    return render(request, "food/index.html", {'item_list': item_list})


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, "food/detail.html", context)


def create_Item(request):
    form = ItemForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, "food/item-form.html", context)


def update_item(request, id):
    item = Item.objects.get(id=id)

    form = ItemForm(request.POST or None, instance=item)
    context = {"form": form, "item": item}

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, "food/item-form.html", context)


def delete_item(request, pk):
    item = Item.objects.get(pk=pk)

    context = {"item": item}

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, "food/delete_item.html", context)




# CLASS BASE VIEW

# case of INDEX

from django.views.generic.list import ListView


class IndexClassView(ListView):
    model = Item;
    template_name = "food/index.html"
    context_object_name = "item_list"


# 🚩🚩🚩🚩🚩VIDEO 58🚩🚩🚩🚩🚩 # CLASS BASE URLS # -> for detail
# case of Details

from django.views.generic.detail import DetailView


class DetailClassView(DetailView):
    model = Item
    template_name = "food/detail.html"


# This is a class base view for create_Item

from django.views.generic.edit import CreateView


from django.urls import reverse_lazy

class create_Item_View(CreateView):
    model = Item
    fields = ['item_name', 'item_describe', 'item_price', 'item_image']
    template_name = "food/item-form.html"

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Par exemple, rediriger vers la page de détails de l'item créé
        return reverse_lazy('food:detail', kwargs={'pk': self.object.pk})


#
# from django.urls import reverse_lazy
#
# class create_Item_View(CreateView):
#     model = Item
#     fields = ['item_name', 'item_describe', 'item_price', 'item_image']
#     template_name = "food/item-form.html"
#     success_url = reverse_lazy('food:index')  # Redirection vers la page d'accueil après création
#
#     def form_valid(self, form):
#         form.instance.user_name = self.request.user
#         return super().form_valid(form)





























# /////////////////////////////////////////////
def item(request):
    return HttpResponse('<h1>Items Banner</h1>')


def ordinateur(request):
    return HttpResponse('les ordinateurs de brenda')


def periferiques(request):
    return HttpResponse('les pefireriques')


def uc(request):
    return HttpResponse('les uc')


def soureis(request):
    return HttpResponse('les soureis')


def titre1(request):
    return HttpResponse('titre1')


def titre2(request):
    return HttpResponse('titre2')


def titre3(request):
    return HttpResponse('titre3')


def titre4(request):
    return HttpResponse('titre4')


def titre5(request):
    return HttpResponse('titre5')


def titre6(request):
    return HttpResponse('titre6')


def titre7(request):
    return HttpResponse('titre7')
