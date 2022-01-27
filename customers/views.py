from django.shortcuts import render,redirect
from .forms import CustomerModelForm

# Create your views here.
# Create your views here.
def home(request):
    if request.method == 'POST':
        customer = CustomerModelForm(request.POST)
        if customer.is_valid():
            valid_data = customer.cleaned_data
            customer.save()
            return redirect('/')
        else:
            return render(request,'customers/index.html')
    else:
        customer = CustomerModelForm()
        return render(request,'customers/index.html')