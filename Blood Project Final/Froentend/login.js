const handleRegistration = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    // const confirm_password = getValue("confirm_password");
    const info = {
      username,
      first_name,
      last_name,
      email,
      password,
    };
  
    if (password) {
      document.getElementById("error").innerText = "";
      if (
        /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(
          password
        )
      ) {
        console.log(info);
  
        fetch("https://blood-donation-awo3.onrender.com/api/auth/register/", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(info),
        })
          .then((res) => res.json())
          .then((data) => console.log(data));
      } else {
        document.getElementById("error").innerText =
          "pass must contain eight characters, at least one letter, one number and one special character:";
      }
    } else {
      document.getElementById("error").innerText =
        "password and confirm password do not match";
      alert("password and confirm password do not match");
    }
  };
  
const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
  };
  
  const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("login-username");
    const password = getValue("login-password");
    console.log(username, password);
    if ((username, password)) {
        console.log("Hi on fetch")
      fetch("https://blood-donation-awo3.onrender.com/api/auth/login/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ username, password }),
      })
        .then((res) => res.json())
        .then((data) => {
            console.log("Hi on post json")
          console.log(data);
          console.log(data.token,"Token data")
          console.log(data.user_id,"userid data")
  
          if (data.token && data.user_id) {
            console.log("Hi")
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user_id);
            console.log(data.token,"Token data")
          console.log(data.user_id,"userid data")
            // window.location.href = "index.html";
          }
        });
    }
  };
  const handlelogOut = (event) => {
    const token = localStorage.getItem("token");
  
    fetch("https://blood-donation-awo3.onrender.com/api/auth/logout/", {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        localStorage.removeItem("token");
        localStorage.removeItem("user_id");
      });
  };
  const loadAllEvents = () => {
    const token = localStorage.getItem("access_token"); // Retrieve token from localStorage or sessionStorage

fetch("https://blood-donation-awo3.onrender.com/api/events/", {
    method: "GET",
    headers: {
        "Authorization": `Bearer ${token}`,  // Include the token
        "Content-Type": "application/json"
    }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error))};

  
  loadAllEvents();