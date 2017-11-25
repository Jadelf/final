from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Plato, Menu, Asignacion
from .forms	import MenuForm
from django.contrib.auth.decorators	import login_required

#Views de menu
def menu_list(request):
    posts = Menu.objects.filter(register_date__lte=timezone.now()).order_by('register_date')
    return render(request, 'blog/menu_list.html',{'posts':posts})

def menu_detail(request,pk):
    post = get_object_or_404(Menu,pk=pk)
    datos=[]
    pl=Asignacion.objects.filter(menu_id=pk)
    for eq in pl:
        nplato = Plato.objects.get(pk=eq.plato_id)
        datos.append(nplato)
    return render(request,'blog/menu_detail.html',{'post':post,'datos':datos})

def	menu_new(request):
	form = MenuForm()
	return render(request,'blog/menu_edit.html',{'form':form})

def menu_new(request):
    if request.method =="POST":
        form = MenuForm(request.POST)
        e = request.POST.getlist('platos')
        p = Plato.objects.all()
        if form.is_valid():
            menu = Menu.objects.create(nombre=form.cleaned_data['nombre'],precio=form.cleaned_data['precio'],empleado=form.cleaned_data['empleado'],cliente=form.cleaned_data['cliente'])
            for plato_id in request.POST.getlist('platos'):
                asignacion = Asignacion(plato_id=plato_id,menu_id = menu.id)
                asignacion.save()
        return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request,'blog/menu_edit.html',{'form':form})
