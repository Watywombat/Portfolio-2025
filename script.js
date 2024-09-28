const form = document.getElementById('contact-form');
const responseMessage = document.getElementById('response-message');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(form);
    
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    }).then(response => {
        if (response.ok) {
            responseMessage.textContent = 'Thank you for your message! I will get back to you soon.';
            form.reset(); 
        } else {
            responseMessage.textContent = 'There was a problem sending your message. Please try again.';
        }
    }).catch(error => {
        responseMessage.textContent = 'There was a problem sending your message. Please try again.';
    });
});
