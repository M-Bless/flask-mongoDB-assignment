/**document.getElementById('forgotPasswordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    
    fetch('/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error('Error:', error));
});
*/

// Temporary storage (Replace with a database or API in a real app)
const users = [
    { regNo: "12345", phone: "1234567890", email: "user1@example.com", address: "123 Street, City" },
    { regNo: "67890", phone: "0987654321", email: "user2@example.com", address: "456 Avenue, City" }
];

// Function to search for a user's phone number by registration number
function searchContact() {
    let regNoInput = document.getElementById("searchRegNo");
    
    let regNo = regNoInput.value.trim();
    let user = users.find(user => user.regNo === regNo);

    if (user) {
        // Display the phone number dynamically
        let phoneLabel = document.querySelector("label[for='phone']");
        phoneLabel.textContent = `Mobile Phone Number: ${user.phone}`;

        // Indicate success with a green border
        regNoInput.style.border = "2px solid green";
    } else {
        // Indicate search failure
        alert("User not found!");
        regNoInput.style.border = "2px solid red";

        // Clear the label text
        let phoneLabel = document.querySelector("label[for='phone']");
        phoneLabel.textContent = "Mobile Phone Number:";
    }
}

// Function to validate login
function validateLogin() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (!username || !password) {
        alert("Please fill in all fields.");
        return;
    }

    fetch('/validate-login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "form.html"; // Redirect to form.html after successful login
        } else {
            alert("Invalid credentials. Try again.");
        }
    })
    .catch(error => console.error('Error:', error));
}
