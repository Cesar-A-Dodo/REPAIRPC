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

}