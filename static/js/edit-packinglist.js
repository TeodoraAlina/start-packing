// Function to toggle the visibility of the task list when clicking on the list title
function toggleList(button) {
    const taskListRow = button.closest('tr').nextElementSibling;
    taskListRow.classList.toggle('hidden');
}

// Function to display a confirmation dialog before deleting an item
function confirmDelete(itemTitle, itemId, itemType) {
    Swal.fire({
        title: `Are you sure you want to delete "${itemTitle}"?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d64a58',
        cancelButtonColor: '#3f9481',
        confirmButtonText: 'Delete',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            // Redirect to the appropriate URL for deleting the item based on its type (packinglist or task)
            if (itemType === 'packinglist') {
                window.location.href = `/delete_item/packinglist/${itemId}/`;
            } else if (itemType === 'task') {
                window.location.href = `/delete_item/task/${itemId}/`;
            }
        }
    });
}