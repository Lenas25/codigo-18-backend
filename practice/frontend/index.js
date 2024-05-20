const nombreInput = document.getElementById('nombre');
const precioInput = document.getElementById('precio');
const agregar = document.getElementById('agregar-btn');
const BACK_URL = 'http://localhost:5000';
const tabla = document.getElementById('tabla');

const tablaHeader = document.createElement('tr');
tablaHeader.innerHTML = `
    <th>id</th>
    <th>nombre</th>
    <th>precio</th>`;

const agregarUsuario = async (data) => {
    const resultado = await fetch(`${BACK_URL}/productos`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    await resultado.json();
    await listarUsuarios();
}

const listarUsuarios = async () => {
    const resultado = await fetch(`${BACK_URL}/productos`, {method: 'GET'});
    const data = await resultado.json();
    tabla.innerHTML = '';
    tabla.appendChild(tablaHeader);

    data.content.forEach((producto, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${index}</td>
            <td>${producto.nombre}</td>
            <td>${producto.precio}</td>`;
        tabla.appendChild(tr);
    });
}

listarUsuarios();

agregar.addEventListener('click', (e) => {
    e.preventDefault();

    if (!nombreInput.value || !precioInput.value) {
        return alert('Por favor, llene todos los campos');
    }

    const data = {
        nombre: nombreInput.value,
        precio: precioInput.value
    }
    agregarUsuario(data);

})