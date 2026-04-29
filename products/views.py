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
            return redirect("home")
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})


@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm (request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user 
            category.save()            
            return redirect("home")
    else:
        form = CategoryForm()

    return render(request, "products/add_category.html", {"form": form})



from django.shortcuts import get_object_or_404

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm(instance=product)

    return render(request, "products/edit_product.html", {"form": form})




@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, owner=request.user)

    if request.method == "POST":
        product.delete()
        return redirect("home")

    return render(request, "products/confirm_delete.html", {"product": product})