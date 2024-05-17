from django.shortcuts import render, redirect

from .models import Product, Cart
from .forms import ProductForm
from accounts.models import CustomUser


# Create your views here.
def index(request):
    """
    This view returns homepage. The startting point of our ecommerce website
    """
    return render(request, 'index.html')


def create_product(request):
    """
    This view create product. User need to supply name, price, image(optional), description(optional)

    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
            context = {
                "form": form
            }
            return render(request, 'ecommerce_app/product_create.html', context=context)

    form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'ecommerce_app/product_create.html', context=context)


def list_products(request):
    """
    Provide List of Users.
        - It gives option to select products and add it into cart
    """
    products = Product.objects.all()

    # search product based on query
    query = request.GET.get("q", "")
    if query:
        products = products.filter(name__icontains=query)

    # sort product based on parameter
    sort_by = request.GET.get("sort_by")
    if sort_by:
        if sort_by == 'name_asc':
            products = products.order_by("name")
        elif sort_by == 'name_desc':
            products = products.order_by("-name")
        elif sort_by == 'price_asc':
            products = products.order_by("price")
        elif sort_by == 'price_desc':
            products = products.order_by("-price")

    context = {
        "products": products,
        "query": query,
        "sort_by": sort_by
    }
    return render(request, 'ecommerce_app/product_list.html', context)


def view_cart_products(request):
    """
    Provide list products inside cart
        - User can remove products which they don't want to buy
    """
    user_email = request.session.get('user_email')
    if user_email:
        user = CustomUser.objects.filter(email=user_email).first()
        cart = Cart.objects.filter(user=user).first()

        cart_products = cart.products.all()

        context = {
            'cart_products': cart_products
        }
        return render(request, 'ecommerce_app/cart_products.html', context)
    else:
        return redirect('accounts:login')


def add_products_to_cart(request):
    """
    Add product to cart
    """
    product_ids = request.POST.getlist('selected_product_ids', [])
    user_email = request.session.get('user_email')
    product_list = []

    if user_email:
        user = CustomUser.objects.filter(email=user_email).first()

        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            product_list.append(product)

        user.cart_user.products.add(*product_list)

        return redirect('ecommerce_app:view_cart_products')
    else:
        return redirect('accounts:login')


def remove_products_from_cart(request):
    """
    Remove product from cart
    """
    product_ids = request.POST.getlist('selected_product_ids', [])
    user_email = request.session.get('user_email')
    product_list = []

    user = CustomUser.objects.filter(email=user_email).first()

    for product_id in product_ids:
        product = Product.objects.get(id=product_id)
        product_list.append(product)

    user.cart_user.products.remove(*product_list)

    return redirect('ecommerce_app:view_cart_products')
