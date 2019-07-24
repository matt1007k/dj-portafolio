from django.shortcuts import render


def Home(request):
    context = {

    }
    return render(request, 'index.html', context)
