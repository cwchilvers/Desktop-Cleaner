function organize_hdlr() {
    var statusElement = document.getElementById('status');
    statusElement.innerText = "Cleaning up...";

    fetch('/organize')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                statusElement.innerText = data.message;
            } else {
                statusElement.innerText = data.message;
            }
        })
        .catch(error => {
            statusElement.innerText = "An error occurred during the cleaning process.";
            console.error('Error:', error);
        });
}