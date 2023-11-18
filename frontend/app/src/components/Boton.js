import estilos from "./Boton.module.css";

export default function Boton() {
  return (
    <button type="button" className={estilos.peligro}>
      Borrar
    </button>
  );
}