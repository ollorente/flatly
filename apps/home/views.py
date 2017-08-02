from django.shortcuts import render


def indexHome(request):
    us = 'Home'
    context = {
        'us':us,
    }
    return render(request, 'home/index.html', context)
