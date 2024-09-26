from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, ComboFamiliar
from .forms import PizzaForm, AlitaForm, BebidaForm, ComboFamiliarForm
from carrito.carrito import Carrito

def menu(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}

    # Inicializar el carrito
    carrito = Carrito(request)

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)

        if producto.categoria.nombre_categoria == 'CombosFamiliares':
            form = ComboFamiliarForm(request.POST)
            if form.is_valid():
                combo_form = form.cleaned_data
                carrito.agregar(
                    producto=producto, 
                    cantidad=1, 
                    sabor_1=combo_form['pizza_sabor_1'], 
                    sabor_2=combo_form['pizza_sabor_2'], 
                    sabor_alita_1=combo_form['alita_sabor_1'], 
                    sabor_alita_2=combo_form['alita_sabor_2'], 
                    sabor_bebida=combo_form['bebida_sabor']
                )
                return redirect('menu')

        elif producto.categoria.nombre_categoria == 'Pizzas':
            form = PizzaForm(request.POST)
            if form.is_valid():
                pizza_form = form.cleaned_data
                carrito.agregar(
                    producto=producto, 
                    cantidad=1, 
                    sabor_1=pizza_form['sabor_1'], 
                    sabor_2=pizza_form['sabor_2']
                )
                return redirect('menu')

        elif producto.categoria.nombre_categoria == 'Alitas':
            form = AlitaForm(request.POST)
            if form.is_valid():
                alita_form = form.cleaned_data
                carrito.agregar(
                    producto=producto, 
                    cantidad=1, 
                    sabor=alita_form['sabor_1']
                )
                return redirect('menu')

        elif producto.categoria.nombre_categoria == 'Bebidas':
            form = BebidaForm(request.POST)
            if form.is_valid():
                bebida_form = form.cleaned_data
                carrito.agregar(
                    producto=producto, 
                    cantidad=1, 
                    sabor=bebida_form['sabor']
                )
                return redirect('menu')

        # Manejo para la categoría "Platos"
        elif producto.categoria.nombre_categoria == 'Platos':
            # Agregar directamente al carrito
            carrito.agregar(producto=producto, cantidad=1)
            return redirect('menu')

    else:
        # Si no se envía un POST o hay un error en la validación, mostrar formularios vacíos
        context['combo_form'] = ComboFamiliarForm()
        context['pizza_form'] = PizzaForm()
        context['alita_form'] = AlitaForm()
        context['bebida_form'] = BebidaForm()

    return render(request, 'menu/menu.html', context)
