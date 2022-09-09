const API_URL = "http://127.0.0.1:8000";

const signup = async (email, name, password, password2) => {

  const response = await fetch(API_URL + "/api/user/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      name: name,
      password: password,
      password2: password2,
    }),
  });
  if (response.data.msg === "Registration Successful") {
    localStorage.setItem("user", JSON.stringify(response.data.token));
  }

  return response.data.token;
};

const login = async (username, password) => {

  const response = await fetch(API_URL + "/api/user/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  });
  if (response.data.msg === "Login Success") {
    localStorage.setItem("user", JSON.stringify(response.data.token));
  }
  return response.data.token;
};

const logout = () => {
  localStorage.removeItem("user");
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem("user"));
};

const authService = {
  signup,
  login,
  logout,
  getCurrentUser,
};

export default authService;
