from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def order_selection_view(request):
    return render(request, 'user_create_order.html', context={})


@login_required
def submit_order_view(request):
    if request.method == 'POST':
        drink_name = request.POST['drink_sale']
        print("\n" + drink_name + "\n")
    return render(request, 'sales_buttons.html')
