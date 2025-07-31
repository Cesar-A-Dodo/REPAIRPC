function add_maquina() {
    const container = document.getElementById('form-maquina');
    const valorAntigo = container.getAttribute('data-maquina') || '';  // pega do atributo

    const html = `
        <br>
        <div class='row'>
            <div class='col-md'>
                <textarea placeholder='Descrição da máquina' class='form-control' name='maquina' rows='4'>${valorAntigo}</textarea>
            </div>
        </div>
    `;

    container.innerHTML = html;
    container.style.display = 'block';
}

function exibir_form(tipo){
    const add_cliente = document.getElementById('adicionar-cliente');
    const att_cliente = document.getElementById('att_cliente');

    if(tipo == "1"){
        att_cliente.style.display = "none";
        add_cliente.style.display = "block";
    } else if(tipo == "2"){
        att_cliente.style.display = "block";
        add_cliente.style.display = "none";
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
        nome.value = data['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['cpf']

        email = document.getElementById('email')
        email.value = data['email']

    })
}