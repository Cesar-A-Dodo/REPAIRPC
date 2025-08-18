import json
import re

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Cliente, Maquina


def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, "clientes.html", {"clientes": clientes_list})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        maquinas = request.POST.getlist("maquina")

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(
                request,
                "clientes.html",
                {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "email": email,
                    "maquina": maquinas or [],
                },
            )

        if not re.fullmatch(
            re.compile(
                r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
            ),
            email,
        ):
            return render(
                request,
                "clientes.html",
                {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "cpf": cpf,
                    "maquina": maquinas or [],
                },
            )

        cliente = Cliente(nome=nome, sobrenome=sobrenome, email=email, cpf=cpf)

        cliente.save()

        for m in maquinas:
            maq = Maquina(maquina=m, cliente=cliente)

            maq.save()

        return HttpResponse("test")


def att_cliente(request):
    id_cliente = request.POST.get("id_cliente")

    cliente = Cliente.objects.filter(id=id_cliente)
    maquinas = Maquina.objects.filter(cliente=cliente[0])

    clientes_json = json.loads(serializers.serialize("json", cliente))[0]["fields"]
    maquinas_json = json.loads(serializers.serialize("json", maquinas))
    maquinas_json = [{"fields": i["fields"], "id": i["pk"]} for i in maquinas_json]
    data = {"cliente": clientes_json, "maquinas": maquinas_json}

    return JsonResponse(data)


@csrf_exempt
def update_maquina(request, id):
    sel_maquina = request.POST.get("maquina")
    maquina = Maquina.objects.get(id=id)
    maquina.maquina = sel_maquina

    maquina.save()
    return HttpResponse("Dados alterados com sucesso!")


def excluir_maquina(request, id):
    try:
        maquina = Maquina.objects.get(id=id)
        maquina.delete()
        return redirect(reverse("clientes") + f"?aba=att_cliente&id_cliente={id}")
    except:
        return redirect(reverse("clientes") + f"?aba=att_cliente&id_cliente={id}")
