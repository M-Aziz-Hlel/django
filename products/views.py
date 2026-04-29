from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import CategoryForm, ProductForm
from .models import Product




@login_required
def my_products(request):
    products = Product.objects.filter(owner=request.user)

    return render(request, "products/my_products.html", {
        "products": products
    })




@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("my-products")
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})


@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm (request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoryForm()

    return render(request, "products/add_category.html", {"form": form})

