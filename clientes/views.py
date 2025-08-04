from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Maquina
import re
from django.core import serializers
import json

def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        maquina = request.POST.getlist('maquina')

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

        for m in maquina:
            maq = Maquina(maquina=m, cliente=cliente)

            maq.save()

        return HttpResponse('test')

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    
    cliente = Cliente.objects.filter(id=id_cliente)
    maquinas = Maquina.objects.filter(cliente=cliente[0])
    
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    maquinas_json = json.loads(serializers.serialize('json', maquinas))
    print(maquinas_json)
    return JsonResponse(cliente_json)