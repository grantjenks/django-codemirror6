from django.shortcuts import render


def demo(request):
    return render(request, 'cm6/demo.html')
