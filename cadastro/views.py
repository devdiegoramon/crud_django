from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

# Listar todos os clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadastro/listar_clientes.html', {'clientes': clientes})

# Criar novo cliente
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastro/cliente_form.html', {'form': form})

# Editar cliente existente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cadastro/cliente_form.html', {'form': form})

# Excluir cliente
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('listar_clientes')
