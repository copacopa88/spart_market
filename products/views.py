from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from .forms import ProductForm, CommentForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

def index(request):
     products= Product.objects.all().order_by('-id')
     context = {
         'products': products,
         }
     return render(request, 'products/index.html', context)




def product_creats(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid(): 
            product=form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('products:product_detail', product.pk)
    else:
        form = ProductForm()
    
    context= {'form':form}
    return render(request, 'products/product_creats.html', context)


@require_POST
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_authenticated:
        if product.author == request.user:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
    return redirect("products:index")



def product_detail(request,pk):
    product=get_object_or_404(Product, id=pk)
    comment_form=CommentForm()
    comments = product.comments.all().order_by('-pk')
    context = {
        'product':product,
        'comment_form':comment_form,
        'comments' : comments,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.author == request.user:
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect("products:product_detail", product.pk)
        else:
            form = ProductForm(instance=product)
    else:
        return redirect("products:index")

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/product_update.html", context)

@require_POST
def comment_create(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.user = request.user #로그인 했을시만 글쓰기 버튼 보이게
        comment.save()
    return redirect("products:product_detail", product.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect('products:product_detail' , pk)

@require_POST    
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('products: index')
    return redirect('accounts:login')