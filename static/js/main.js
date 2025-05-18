document.addEventListener('DOMContentLoaded', function() {
    fetchTodos();

    document.getElementById('add-todo').addEventListener('click', function() {
        const todoText = document.getElementById('todo-input').value;
        if (todoText) {
            addTodo({ text: todoText });
            document.getElementById('todo-input').value = '';
        }
    });
});

function fetchTodos() {
    fetch('/todos')
        .then(response => response.json())
        .then(data => {
            const todoList = document.getElementById('todo-list');
            todoList.innerHTML = '';
            data.forEach(todo => {
                const li = document.createElement('li');
                li.className = 'todo-item';
                li.innerHTML = `${todo.text} <button onclick="deleteTodo('${todo._id}')">Delete</button>`;
                todoList.appendChild(li);
            });
        });
}

function addTodo(todo) {
    fetch('/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(todo)
    }).then(() => {
        fetchTodos();
    });
}

function deleteTodo(id) {
    fetch(`/todos/${id}`, {
        method: 'DELETE'
    }).then(() => {
        fetchTodos();
    });
}