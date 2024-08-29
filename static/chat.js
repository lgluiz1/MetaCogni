
        async function sendMessage() {
            let userMessage = document.getElementById('userMessage').value;
            let response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `message=${userMessage}`
            });
            let data = await response.json();
            document.getElementById('chatbox').innerHTML += `<p>Você: ${userMessage}</p>`;
            document.getElementById('chatbox').innerHTML += `<p>Chatbox: ${data.response}</p>`;
        }
   