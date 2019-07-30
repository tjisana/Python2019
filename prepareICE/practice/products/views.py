from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm


def product_detail_view(request, my_id):
    context = dict()
    try:
        obj = Product.objects.get(id=my_id)
        context['obj'] = obj
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'product/form_test.html', context=context)
    # return render(request, 'product/detail.html', context={'object': Product.objects.get(id=1)})


# def product_create_view(request):
#     initial = {'title': "my awesome title"}
#     obj = Product.objects.get(id=1)
#     # form = ProductForm(request.POST or None, initial=initial, instance=obj)
#     form = ProductForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     return render(request, 'product/form_test.html', context={'form': form})
#     # return render(request, 'product/product_create.html', context={'form': form})

# def product_create_view(request, my_id):
#     # obj = Product.objects.get(id=my_id)
#     # obj = get_object_or_404(Product, id=my_id)
#     try:
#         obj = Product.objects.get(id=my_id)
#     except Product.DoesNotExist:
#         raise Http404
#     return render(request, 'product/form_test.html', context={'obj': obj})

def product_create_view(request):
    object_list = Product.objects.all()
    return render(request, 'product/form_test.html', context={'object_list': object_list})
