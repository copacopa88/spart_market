from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from .forms import ProductForm, CommentForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

def index(request):
     indexs= Product.objects.all().order_by('-id')
     context = {
         'indexs': indexs,
         }
     return render(request, 'products/index.html', context)




def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid(): 
            product=form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_detail', product.pk)
    else:
        form = ProductForm()
    
    context= {'form':form}
    return render(request, 'create.html', context)

def product_detail(request,pk):
    product=get_object_or_404(Product, id=pk)
    comment_form=CommentForm()
    comments = product.comments.all().order_by('-pk')
    context = {
        'product':product,
        'comment_form':comment_form,
        'comments' : comments,
    }
    return render(request, 'product_detail.html', context)