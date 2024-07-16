function compileCode() {
    let code = document.getElementById('code').value;
  
    fetch('/compile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
      // Update the output area with the received output
      document.getElementById('output').textContent = data.output;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  