const errorMessage = document.getElementById('error-mes');
        
        // Add an event listener to the form submission
        document.getElementById('login-form').addEventListener('submit', async (e) => {
            e.preventDefault(); // Prevent the form from submitting
            
            const form = e.target;
            const formData = new FormData(form);
            
            try {
                const cum = await fetch('http://localhost:8000/loginauth', {
                    method: 'POST',
                    body: formData,
                });
                if (cum.ok) {
                    window.location.href = 'http://localhost:3000/';
                } else {
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('An error occurred:', error);
            }
        });