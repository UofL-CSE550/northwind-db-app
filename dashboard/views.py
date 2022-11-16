from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Customer, Product, Order, OrderDetail, Invoice


# Create your views here.
def index(request):
    return render(request, 'index.html')


def customer_list(request):
    customer_list_obj = Customer.objects.all()
    page, customers = list_pagination(customer_list_obj, request)

    context = {
        'page': page,
        'customers': customers
    }
    return render(request, 'customer/list.html', context)


def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    customer_orders_obj = Order.objects.filter(customer_id=id)
    page, customer_orders = list_pagination(customer_orders_obj, request)

    context = {
        'customer': customer,
        'page': page,
        'customer_orders': customer_orders
    }
    return render(request, 'customer/detail.html', context)


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
    order_details_obj = OrderDetail.objects.filter(order_id=id)
    page, order_details = list_pagination(order_details_obj, request)
    try:
        invoice = Invoice.objects.get(order_id=id)
    except Invoice.DoesNotExist:
        invoice = None

    context = {
        'order': order,
        'order_details': order_details,
        'page': page,
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
