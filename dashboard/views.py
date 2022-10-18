from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Product, Order, OrderDetail, Invoice


# Create your views here.
def index(request):
    return render(request, 'index.html')


def product_list(request):
    object_list = Product.objects.all()
    page, products = list_pagination(object_list, request)

    context = {
        'page': page,
        'products': products
    }
    return render(request, 'product/list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)


def order_list(request):
    all_order_obj = Order.objects.all()
    page, orders = list_pagination(all_order_obj, request)

    context = {
        'page': page,
        'orders': orders
    }
    return render(request, 'order/list.html', context)


def order_detail(request, id):
    order = Order.objects.get(id=id)
    order_details = OrderDetail.objects.filter(order_id=id)
    invoice = Invoice.objects.get(order_id=id)

    context = {
        'order': order,
        'order_details': order_details,
        'invoice': invoice
    }
    return render(request, 'order/detail.html', context)


def list_pagination(object_list, request):
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        entities = paginator.page(page)
    except PageNotAnInteger:
        entities = paginator.page(1)
    except EmptyPage:
        entities = paginator.page(paginator.num_pages)
    return page, entities
