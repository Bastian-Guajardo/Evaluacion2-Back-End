from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuego
from .forms import VideojuegoForm

# 1. LEER (Listar todos los videojuegos)
def lista_videojuegos(request):
    juegos = Videojuego.objects.all()
    return render(request, 'catalogo/tienda.html', {'juegos': juegos})

# 2. CREAR (Formulario de Ingreso)
def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'catalogo/crear.html', {'form': form})

# 3. MODIFICAR / EDITAR (Formulario de Edición)
def editar_videojuego(request, id):
    juego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=juego)
    return render(request, 'catalogo/editar.html', {'form': form, 'juego': juego})

# 4. ELIMINAR 
def eliminar_videojuego(request, id):
    juego = get_object_or_404(Videojuego, id=id)
    if request.method == 'POST':
        juego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'catalogo/eliminar.html', {'juego': juego})

