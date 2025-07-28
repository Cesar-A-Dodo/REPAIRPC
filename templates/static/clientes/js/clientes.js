function add_maquina() {
    container = document.getElementById('form-maquina')
    
    html = `
        <br>
        <div class='row'>
            <div class='col-md'>
                <textarea placeholder='Descrição da máquina' class='form-control' name='maquina' rows='4'></textarea>
            </div>
        </div>
    `

    container.innerHTML = html
}