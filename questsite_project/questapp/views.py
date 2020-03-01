from django.shortcuts import render
from questapp.models import Place

# Create your views here.


def play_form(request):
    response_vars = {}
    if 'code_input' in request.GET:
        code_input = request.GET['code_input']
        try:
            pl = Place.objects.get(code=code_input)
            response_vars = {'pl': pl}
        except Place.DoesNotExist:
            print('nf')
    return render(request, 'play_form.html', response_vars)
