from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html') 
    context = {
        'item_list': item_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse('<h1>This is an Item view</h1>')

def detail_view(request, item_id):
  item = Item.objects.get(pk=item_id)
  context = {
    'item': item,
  }
  # return HttpResponse("This is item no/id: %s" % item_id)
  return render(request, 'food/detail.html', context)

# Form
def create_item(request):
   form = ItemForm(request.POST or None)
#    context = {
#       'form':form
#    }

   if form.is_valid():
      form.save()
      return redirect('index')
   
   return render(request, 'food/item_form.html', {'form':form})

#update item

def update_item(request, item_id):
   item = Item.objects.get(pk=item_id)
   form = ItemForm(request.POST or None, instance=item)

   context = {
      'form': form,
      'item':item,
   }

   if form.is_valid():
      form.save()
      return redirect('index')
   return render(request, 'food/item_form.html',context)
#    return render(request, 'food/item_form.html',{'form':form, 'item':item})

def delete_item(request, item_id):
   item = Item.objects.get(pk=item_id)
   
   if request.method == 'POST':
      item.delete()
      return redirect('index')
   return render(request, 'food/item_delete.html', {'item':item})




   

