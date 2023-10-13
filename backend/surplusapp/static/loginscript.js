const errorMessage = document.getElementById('error-mes');

// Add an event listener to the form submission
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the form from submitting

    const form = e.target;
    const formData = new FormData(form);

    try {
        const r = await fetch('http://localhost:8000/loginauth', {
            method: 'POST',
            body: formData,
        });
        if (r.ok) {
            window.location.href = 'http://localhost:3000/';
        } else if (r.status === 500) {
            // Display the server error message
            errorMessage.innerText = 'Server Error: Please try again later.';
            errorMessage.style.display = 'block';
        } else {
            // Display a default error message
            errorMessage.innerText = 'Invalid credentials. Please try again.';
            errorMessage.style.display = 'block';
        }
    } catch (error) {
        // Display the error message and log the error
        errorMessage.innerText = `An error occurred: ${error.message}`;
        errorMessage.style.display = 'block';
        console.error('An error occurred:', error);
    }
});
