from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .models import Category, SubCategory, Products
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
def index(request):
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


class ProductCreateView(CreateView):
    model = Products
    fields = '__all__'
    form = ProductForm
    template_name = 'products/product-form.html'
    success_url = reverse_lazy('products:index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context
    
    def form_valid(self, form) -> HttpResponse:
        self.instance = form.save(commit=False)
        self.instance.category_id = self.request.POST.get('category')
        self.instance.subcategory_id = self.request.POST.get('subcategory')
        self.instance.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Products
    template_name = 'products/products-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        super().get_queryset()
        slug = self.request.resolver_match.kwargs['subcat_slug']
        queryset = Products.objects.filter(subcategory__slug = slug)
        return queryset
    