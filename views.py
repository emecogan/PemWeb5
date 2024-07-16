from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from myFirstApp.models import AccountUser

# Create your views here.def readStudent(request):
    data = AccountUser.objects.all()

    context = {'data_list': data}

    return render(request, 'index.html', context)
