function add_maquina() {
    container = document.getElementById('form-maquina')

    html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='Descrição da máquina' class='form-control' name='maquina'> </div> </div>"

    container.innerHTML += html
}

function exibir_form(tipo){
    
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if(tipo == "1"){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    } else if(tipo == "2"){
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
    }
}

function dados_cliente(){
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){

        document.getElementById('form-att-cliente').style.display = 'block'

        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']

        email = document.getElementById('email')
        email.value = data['cliente']['email']
        
        div_maquinas = document.getElementById('maquinas')
        
        div_maquinas.innerHTML = ""
        for (i = 0; i < data['maquinas'].length; i++) {
            valor = data['maquinas'][i]['fields']['maquina']
            div_maquinas.innerHTML += "<form action='/clientes/update_maquina/" + data['maquinas'][i]['id'] + "' method='POST'>\
                <div class='row'>\
                    <div class='col-md'>\
                        <input class='form-control' type='text' name='maquina' value='" + data['maquinas'][i]['fields']['maquina'] + "'>\
                    </div>\
                    <div class='col-md'>\
                        <input class='btn-success' type='submit' value='Salvar'>\
                    </div>\
                    </form>\
                        <a class='btn-danger' href='/clientes/excluir_maquina/" + data['maquinas'][i]['id'] + "'>EXCLUIR</a>\
                </div><br>"
                

        }
    })
}