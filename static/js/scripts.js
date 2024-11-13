// static/js/scripts.js

// Example of simple form validation for add transaction and budget forms
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            let valid = true;
            const inputs = form.querySelectorAll('input, select');

            inputs.forEach(input => {
                if (input.value.trim() === '') {
                    valid = false;
                    input.style.borderColor = 'red';  // Highlight invalid fields
                } else {
                    input.style.borderColor = ''; // Reset border color
                }
            });

            if (!valid) {
                event.preventDefault();
                alert('Please fill out all fields before submitting!');
            }
        });
    });
});
