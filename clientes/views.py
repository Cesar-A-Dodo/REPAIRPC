from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Maquina
import re

def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        maquina = request.POST.get('maquina')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'maquina': maquina})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'maquina': maquina})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        cliente.save()

        maq = Maquina(maquina=maquina, cliente=cliente)

        maq.save()

        return HttpResponse('test')