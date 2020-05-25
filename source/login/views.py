from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm

# Create your views here.

def index(request):
    """A view function for the index page."""
    return render(request, 'index.html')


def get_form(request):
    """View function for getting the form data via post method."""
    if request.method == "POST":
        #This creates an instance of the form and populates with data from the request above.
        form = LoginForm(request.POST)
        if form.is_valid():
        #Checks if form is valid.

            return HttpResponseRedirect("/")
            #Returns to another url

    else: 
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

