from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})
