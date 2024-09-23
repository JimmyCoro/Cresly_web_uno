from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import PizzaForm, AlitaForm, BebidaForm
from carrito.carrito import Carrito    

def menu(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)

        carrito = Carrito(request)

        if producto.categoria.nombre_categoria == 'Pizzas':
            form = PizzaForm(request.POST)
            if form.is_valid():
                pizza_form = form.cleaned_data
                carrito.agregar(producto=producto, cantidad=1, sabor_1=pizza_form['sabor_1'], sabor_2=pizza_form['sabor_2'])
                return redirect('menu')
            
        elif producto.categoria.nombre_categoria == 'Alitas':
            form = AlitaForm(request.POST)
            if form.is_valid():
                alita_form = form.cleaned_data
                carrito.agregar(producto=producto, cantidad=1, sabor_1=alita_form['sabor_1'], sabor_2=alita_form['sabor_2'])
                return redirect('menu')
        
        elif producto.categoria.nombre_categoria == 'Bebidas':
            form = BebidaForm(request.POST)
            if form.is_valid():
                bebida_form = form.cleaned_data
                carrito.agregar(producto=producto, cantidad=1, sabor_1=bebida_form['sabor'])
                return redirect('menu')
            
    context['pizza_form'] = PizzaForm()
    context['alitas_form'] = AlitaForm()
    context['bebida_form'] = BebidaForm()

    return render(request, 'menu/menu.html', context)
