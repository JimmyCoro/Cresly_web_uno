from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import PizzaForm, AlitaForm, BebidaForm

def menu(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)

        if producto.categoria.nombre_categoria == 'Pizzas':
            form = PizzaForm(request.POST)
            if form.is_valid():
                pizza = form.save(commit=False)
                pizza.producto = producto
                pizza.save()
                return redirect('menu')
            
        elif producto.categoria.nombre_categoria == 'Alitas':
            form = AlitaForm(request.POST)
            if form.is_valid():
                alitas = form.save(commit=False)
                alitas.producto = producto
                alitas.save()
                return redirect('menu')
        
        elif producto.categoria.nombre_categoria == 'Bebidas':
            form = BebidaForm(request.POST)
            if form.is_valid():
                alitas = form.save(commit=False)
                alitas.producto = producto
                alitas.save()
                return redirect('menu')
            
    # Para mostrar el formulario en el modal, debes asegurarte de incluir el formulario adecuado en el contexto
    context['pizza_form'] = PizzaForm()
    context['alitas_form'] = AlitaForm()
    context['bebida_form'] = BebidaForm()

    return render(request, 'menu/menu.html', context)
