from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)

def contacts(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print("Новая заявка:")
        print(f"Имя: {name}")
        print(f"Телефон: {phone}")
        print(f"Сообщение: {message}")

        context["success"] = "Сообщение успешно отправлено!"

    return render(request, "contacts.html", context)


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )
