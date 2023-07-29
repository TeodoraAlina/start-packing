function toggleList(button) {
    const taskListRow = button.closest('tr').nextElementSibling;
    taskListRow.classList.toggle('hidden');
}

function confirmDelete(itemTitle, itemId, itemType) {
    if (confirm(`Are you sure you want to delete "${itemTitle}"?`)) {
        // If the user confirms, redirect to the appropriate delete view
        if (itemType === 'packinglist') {
            window.location.href = `/delete_item/packinglist/${itemId}/`;
        } else if (itemType === 'task') {
            window.location.href = `/delete_item/task/${itemId}/`;
        }
    }
}