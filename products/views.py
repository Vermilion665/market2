from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .models import Category, SubCategory, Products
from .forms import CategoryForm, SubCategoryForm, ProductForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return HttpResponse('This is page PRODUCTS')

def root_index(request):
    category = Category.objects.all()
    context = {
        'category_list': category
    }
    return render(request, 'products/index.html', context=context)
    

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    form = CategoryForm
    template_name = 'products/ctegory-form.html'
    success_url = reverse_lazy('products:category-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category-list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        subcategories = SubCategory.objects.all()
        context['subcategories'] = subcategories
        return context
    

class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = '__all__'
    form = SubCategoryForm
    template_name = 'products/subcategory-form.html'
    success_url = reverse_lazy('products:category-list')