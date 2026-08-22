// Seleccionamos elementos
const form = document.getElementById('userInput');
const taskInput = document.getElementById('taskInput');
const listContainer = document.getElementById('list-container');
const stats = document.getElementById('stats');

let tasks = JSON.parse(localStorage.getItem('myTasks')) || [];

function updateUI() {
    listContainer.innerHTML = '';//limpiar o vaciar todo el contenido HTML que hay dentro de listcontainer
    let pendiente = 0;
    let completado = 0;

    tasks.forEach((task, index) => { //para recorrer un arreglo llamado taks osea todo lo q hay en el arreglo task del html
        if (task.completado) completado++;
        else pending++;

        const div = document.createElement('div');
        div.className = 'task-container';
        
        // La estructura HTML debe ser exactamente como la tienes en el CSS
        div.innerHTML = `
            <input type="checkbox" ${task.completado ? 'checked' : ''} onchange="toggleTask(${index})">
            <label>${task.text}</label>
            <img src="img/eliminar.png" alt="Eliminar tarea" class="delete-btn" onclick="deleteTask(${index})">
        `;
        listContainer.appendChild(div);
    });
//actualiza las vistas para que el usuario las vea a el instante 
    stats.innerText = `Tareas pendientes: ${pendiente} | Tareas completadas: ${completado}`;
    localStorage.setItem('myTasks', JSON.stringify(tasks));//se encarga de actualizar el interfas y guardar los cambios permanentemente
}//guardaruna lista de tareas almacenadas en la variable tasks(clave valor)

// Agregar tarea
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = taskInput.value.trim();
    if (text !== '') {
        tasks.push({ text, completado: false });
        taskInput.value = '';
        updateUI();
    }
});

// Cambiar estado
window.toggleTask = (index) => {
    tasks[index].completado = !tasks[index].completed;
    updateUI();
};

// Eliminar tarea
window.deleteTask = (index) => {
    tasks.splice(index, 1);
    updateUI();
};

// Inicializar
updateUI();