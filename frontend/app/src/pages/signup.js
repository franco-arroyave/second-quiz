import { useState } from 'react';
import { signup, signin } from '@/services/backend';
//import styles from 'register.module.css'

export default function Register(){
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const api = signin(username);

    console.log(api);
  };

  return (
    <div>
      <h1>Página de Registro</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Usuario:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label>
          Correo Electrónico:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
};
