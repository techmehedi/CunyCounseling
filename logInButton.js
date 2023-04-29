function checkLogin() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

      if (username && password) {
        // If both fields are set, redirect to the next page
        window.location.href = 'counseling.html';
      } else {
        // If either field is not set, stay on the same page
        alert('Please enter both username and password');
      }
    }