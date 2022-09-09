import { useState, useEffect } from "react";
import { Routes, Route, Link } from "react-router-dom";
import AuthService from "./utils/auth";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Home from "./components/Home";

function App() {
  const [currentUser, setCurrentUser] = useState(undefined);

  useEffect(() => {
    const user = AuthService.getCurrentUser();

    if (user) {
      setCurrentUser(user);
    }
  }, []);

  const logOut = () => {
    AuthService.logout();
  };

  return (
    <div>
      <nav className="">
        <div >
          <li >
            <Link to={"/home"} >
              Home
            </Link>
          </li>

          
        </div>

        {currentUser ? (
          <div>
            <li >
              <a href="/login" onClick={logOut}>
                Logout
              </a>
            </li>
          </div>
        ) : (
          <div >
            <li >
              <Link to={"/login"} >
                Login
              </Link>
            </li>

            <li>
              <Link to={"/signup"}>
                Sign up
              </Link>
            </li>
          </div>
        )}
      </nav>

      <div>
        <Routes>
          <Route exact path="/home" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
