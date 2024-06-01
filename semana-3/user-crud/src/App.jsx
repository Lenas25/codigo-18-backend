import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  // error de cors
  const [users, setUsers] = useState([]);
  const [translate, setTranslate] = useState(0);
  const [inputValues, setInputValues] = useState({
    name: "",
    lastname: "",
    email: "",
    password: "",
    phone_number: "",
    gender: "",
  });

  const handleInputs = (e) => {
    setInputValues({
      ...inputValues,
      [e.target.name]: e.target.value,
    });
  };

  const getUsers = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000");
      const data = await response.json();
      setUsers(data.users);
    } catch (Error) {
      console.log(Error);
    }
  };

  const createUser = async (e) => {
    e.preventDefault();

    if (Object.values(inputValues).some(value => value === "")) {
      console.log("Todos los campos son requeridos");
      return;
    }

    const response = await fetch("http://127.0.0.1:5000/api/v1/user", {
      method: "POST",
      body: JSON.stringify(inputValues),
      headers: {
        "Content-type": "application/json",
      },
    });

    const data = await response.json();

    console.log(data);
    setInputValues({
      name: "",
      lastname: "",
      email: "",
      password: "",
      phone_number: "",
      gender: "",
    });
  };

  const deleteUser = async (user_id) => {
    const response = await fetch(
      `http://127.0.0.1:5000/api/v1/user/${user_id}`,
      {
        method: "DELETE",
        headers: {
          "Content-type": "application/json",
        },
      }
    );

    const data = await response.json();
    console.log(data);
  };

  const back = () => {
    // retroceder con el boton
    if (translate === 0) {
      return;
    }
    setTranslate(translate + 300);
  };

  const next = () => {
    // avanzar con el boton
    setTranslate(translate - 300);
  };

  useEffect(() => {
    const fetchUsers = async () => {
      await getUsers();
    };

    fetchUsers();
  }, [, users]);

  return (
    <>
      <main className="main-container">
        <section>
          <h1>List Users</h1>
          <div
            style={{
              display: "flex",
              gap: 10,
              justifyContent: "center",
              alignItems: "center",
            }}>
            <button onClick={back}>Back</button>
            <button onClick={next}>Next</button>
          </div>
          <div
            className="cards"
            style={{
              transform: `translateX(${translate}px)`,
              transition: "all 0.6s ease-in-out",
            }}>
            {users.map((user) => {
              return (
                <div key={user.id} className="card-user">
                  <h3>Nombre: {user.full_name}</h3>
                  <p>Email: {user.email}</p>
                  <p>Phone: {user.phoneNumber}</p>
                  <p>Gender: {user.gender}</p>
                  <div>
                    <button
                      type="button"
                      style={{ background: "red" }}
                      onClick={() => deleteUser(user.id)}>
                      Delete
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
          <button onClick={getUsers}>Get Users</button>
        </section>
        <section>
          <h2>Create User</h2>
          <form onSubmit={createUser}>
            <div>
              <input
                type="text"
                placeholder="Enter name..."
                name="name"
                value={inputValues.name}
                autoComplete="off"
                onChange={handleInputs}
              />
              <input
                type="text"
                placeholder="Enter lastname..."
                name="lastname"
                value={inputValues.lastname}
                onChange={handleInputs}
              />
            </div>
            <div>
              <input
                type="email"
                placeholder="Enter email..."
                name="email"
                autoComplete="off"
                value={inputValues.email}
                onChange={handleInputs}
              />
              <input
                type="password"
                placeholder="Enter password..."
                autoComplete="off"
                name="password"
                value={inputValues.password}
                onChange={handleInputs}
              />
            </div>
            <div>
              <input
                type="text"
                placeholder="Enter phone number..."
                name="phone_number"
                value={inputValues.phone_number}
                onChange={handleInputs}
              />
              <input
                type="text"
                placeholder="Enter gender (F/M)..."
                name="gender"
                value={inputValues.gender}
                onChange={handleInputs}
              />
            </div>
            <button type="submit">Create New User</button>
          </form>
        </section>
      </main>
    </>
  );
}

export default App;
