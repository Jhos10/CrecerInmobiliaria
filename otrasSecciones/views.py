from django.shortcuts import render

# Create your views here.from django.shortcuts import render

def inmobiliaria_view(request):
    return render(request, 'sobreNosotros.html')

def contactanos(request):
    return render(request,'contactenos.html')

