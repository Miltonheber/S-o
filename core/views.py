from django.shortcuts import render
from .models import Lingua, Pedido, Usuario
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from time import sleep
from .forms import FormPedido

def login(request):

    status = request.GET.get('status')
    contexto = {
            'status':status
            }
    return render(request, 'login.html', contexto)

def home(request):
    status = request.GET.get('status')

    if request.session.get('login'):
        #return HttpResponse('Oky')
        return render(request, 'home.html', {})
    else:
        #return HttpResponse('Faça login')
        return redirect('/?status=3')


def valida_login(request):
    numero = request.POST.get('numero')
    senha = request.POST.get('senha')

    if (numero == None or len(numero.strip()) == 0) or len(senha.strip()) == 0:
        return redirect('/?status=0')
    else:
        if len(numero) != 9:
            return redirect('/?status=1')
        try:
            usuario = Usuario.objects.get(numero=numero, senha=senha)
            print(usuario)

        except:
            return redirect('/?status=0')
        else:
            request.session['login'] = [True, usuario.nome]
            return redirect('/home/?status=0')

def logout(request):
    try:
        del request.session['login']
        return redirect('/?status=2')
    except KeyError:
        return redirect('/?status=3')


def adicionar_pedido(request):
    if request.session.get('login'):
        if request.method == 'POST':
            print(request.POST)
            form = FormPedido(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/adicionar_pedido/?status=0')
            else:
                form = FormPedido(request.POST)
    
        form = FormPedido()
        print(request.GET)
        status = request.GET.get('status')
        contexto = {'form':form, 'status':status}
        return render(request, 'create_pedido.html', contexto)
    else:
        return redirect('/?status=4')


def pedidos(request):
    if request.session.get('login'):
        pedidos_pendentes = Pedido.objects.all()
        status = request.GET.get('status')
        contexto = {'pedidos':pedidos_pendentes, 'status':status}
        return render(request, 'list_pedidos.html', contexto)
        
    else:
        return redirect('/?status=4')


def apagar_pedido(request, pk):
    if request.session.get('login'):
        pedido = get_object_or_404(Pedido, id=pk)
        pedido.delete()
        return redirect('/pedidos/?status=1')
    else:
        return redirect('/?status=4')


def update_pedido(request, pk):
    if request.session.get('login'):
        pedido = get_object_or_404(Pedido, id=pk)

        if request.method == 'POST':
            form = FormPedido(request.POST,instance=pedido)
            if form.is_valid():
                form.save()
                return redirect('/pedidos/?status=0')
            return render(request, 'update_pedido.html', {'form':form})
        
        form = FormPedido(instance=pedido)
        contexto = {'form':form}
        return render(request, 'update_pedido.html', contexto)
    else:
        return redirect('/?status=4')
        

