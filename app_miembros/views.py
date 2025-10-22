from django.shortcuts import render, get_object_or_404, redirect
from .models import Miembro, Membresia
from .forms import MiembroForm, MembresiaForm

def index(request): 
    # Usa index.html
    return render(request, 'index.html')

# --- Vistas para Membresia ---

def lista_membresias(request):
    # Usa lista_membresias.html
    membresias = Membresia.objects.all()
    return render(request, 'lista_membresias.html', {'membresias': membresias})

def detalle_membresia(request, id_membresia):
    # NO USAMOS detalle_membresia.html. Redirigimos a la lista (Listar)
    # Si esta vista es llamada, simplemente redirige para evitar el error de plantilla.
    return redirect('app_miembros:lista_membresias') 
    
def crear_membresia(request):
    # Usa formulario_membresia.html
    if request.method == 'POST':
        form = MembresiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_miembros:lista_membresias')
    else:
        form = MembresiaForm()
    return render(request, 'formulario_membresia.html', {'form': form, 'titulo': 'Crear Membresía'})

def editar_membresia(request, id_membresia):
    # Usa formulario_membresia.html
    membresia = get_object_or_404(Membresia, id_membresia=id_membresia)
    if request.method == 'POST':
        form = MembresiaForm(request.POST, instance=membresia)
        if form.is_valid():
            form.save()
            # Redirige a la lista, ya que no usamos la vista detalle
            return redirect('app_miembros:lista_membresias') 
    else:
        form = MembresiaForm(instance=membresia)
    return render(request, 'formulario_membresia.html', {'form': form, 'titulo': 'Editar Membresía'})

def borrar_membresia(request, id_membresia):
    # Usa confirmar_borrar.html
    membresia = get_object_or_404(Membresia, id_membresia=id_membresia)
    if request.method == 'POST':
        membresia.delete()
        return redirect('app_miembros:lista_membresias')
    # Corregido: Usamos la plantilla genérica confirmar_borrar.html
    # Pasamos 'objeto' y 'tipo' para que la plantilla genérica funcione
    return render(request, 'confirmar_borrar.html', {'objeto': membresia, 'tipo': 'Membresía'}) 

# --- Vistas para Miembro ---

def lista_miembros(request):
    # Usa lista_miembros.html
    miembros = Miembro.objects.all()
    return render(request, 'lista_miembros.html', {'miembros': miembros})

def detalle_miembro(request, id_miembro):
    # NO USAMOS detalle_miembro.html. Redirigimos a la lista (Listar)
    # Si esta vista es llamada, simplemente redirige para evitar el error de plantilla.
    return redirect('app_miembros:lista_miembros')

def crear_miembro(request):
    # Usa formulario_miembro.html
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_miembros:lista_miembros')
    else:
        form = MiembroForm()
    return render(request, 'formulario_miembro.html', {'form': form, 'titulo': 'Crear Miembro'})

def editar_miembro(request, id_miembro):
    # Usa formulario_miembro.html
    miembro = get_object_or_404(Miembro, id_miembro=id_miembro)
    if request.method == 'POST':
        form = MiembroForm(request.POST, instance=miembro)
        if form.is_valid():
            form.save()
            # Redirige a la lista, ya que no usamos la vista detalle
            return redirect('app_miembros:lista_miembros')
    else:
        form = MiembroForm(instance=miembro)
    return render(request, 'formulario_miembro.html', {'form': form, 'titulo': 'Editar Miembro'})

def borrar_miembro(request, id_miembro):
    # Usa confirmar_borrar.html
    miembro = get_object_or_404(Miembro, id_miembro=id_miembro)
    if request.method == 'POST':
        miembro.delete()
        return redirect('app_miembros:lista_miembros')
    # Corregido: Usamos la plantilla genérica confirmar_borrar.html
    # Pasamos 'objeto' y 'tipo' para que la plantilla genérica funcione
    return render(request, 'confirmar_borrar.html', {'objeto': miembro, 'tipo': 'Miembro'})