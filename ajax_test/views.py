from django.shortcuts import render
from .forms import TinyTestForm
from .models import TinyForm
from django.http import JsonResponse

# Create your views here.

def index(request):
    form = TinyTestForm()
    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'index.html', context)

def save(request):
    form = TinyTestForm()
    if request.is_ajax():
        form =TinyTestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {
                'msg': 'Successfully Added User.'
            }
            return JsonResponse(data)
    else:
        return JsonResponse({"msg": "not permitted"})
