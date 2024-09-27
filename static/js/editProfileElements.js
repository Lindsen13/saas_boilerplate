
function toggleEditName() {
    document.getElementById('name-display').classList.add('d-none');
    document.getElementById('name-input').classList.remove('d-none');
    document.getElementById('edit-button-name').classList.add('d-none');
    document.getElementById('save-button-name').classList.remove('d-none');
}

function saveName() {
    const nameInput = document.getElementById('name-input').value;
    fetch(`/update_name?name=${encodeURIComponent(nameInput)}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
        })
        .then(response => response.json())
        .then(data => {
        if (data) {
            console.log('Name updated successfully');
            document.getElementById('name-display').textContent = nameInput;
        } else {
            console.error('Error updating name');
        }
        })
        .catch(error => console.error('Error:', error));
    document.getElementById('name-display').classList.remove('d-none');
    document.getElementById('name-input').classList.add('d-none');
    document.getElementById('edit-button-name').classList.remove('d-none');
    document.getElementById('save-button-name').classList.add('d-none');
}
