document.getElementById("submitButton").addEventListener("click", async () => {
    const number = parseInt(document.getElementById("numberInput").value);
    const resultElement = document.getElementById("result");

    if (isNaN(number)) {
        resultElement.textContent = "Please enter a valid number.";
        return;
    }

    try {
        const response = await fetch('/fizzbuzz', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ number })
        });

        const data = await response.json();
        resultElement.textContent = data.result;
    } catch (error) {
        resultElement.textContent = "An error occurred. Please try again.";
    }
});
