from django.shortcuts import redirect, render
from lists.models import Item,List
from lists.forms import ItemForm, ExistingListItemForm
from django.core.exceptions import ValidationError
from django.views.generic import FormView, CreateView

class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm

class NewListView(CreateView):
    form_class = ItemForm
    template_name = 'home.html'

    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
       list_ = List.objects.create()
       form.save(for_list=list_)
       return redirect(list_)
    else:
       return render(request, 'home.html', {"form": form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)

    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)

    return render(request, 'list.html', { 'list': list_, 'form': form })

def my_lists(request, email):
    return render(request, 'my_lists.html')
