from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def index(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Please fill the form correctly!")

    context = {
        'form': form,
    }
    return render(request, "index.html", context)