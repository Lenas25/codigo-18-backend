/**
 * Para tipar un objeto en TS
 * 1. Interface -> lo cual me permite poder definir los atributos del objeto y el tipo de dato de cada atributo
 * 2. Type -> lo mismo que interface
 */

interface Persona {
  nombre: string;
  apellido: string;
  edad: number;
  dni: number;
  direccion: string;
}

type Persona2 = {
  nombre: string;
  apellido: string;
  edad: number;
  dni: number;
  direccion?: string;
}

const persona: Persona = {
  nombre:"Pepe",
  apellido:"Perez",
  edad: 30,
  dni: 72702637,
  direccion: "Calle 123"
}

const persona2: Persona2 = {
  nombre:"Pepe",
  apellido:"Perez",
  edad: 30,
  dni: 72702637
}

const listaDePersonas: Persona[] = [
  {
    nombre:"Pepe",
    apellido:"Perez",
    edad: 30,
    dni: 72702637,
    direccion: "Calle 123"
  },
  {
    nombre:"Juan",
    apellido:"Perez",
    edad: 30,
    dni: 72702637,
    direccion: "Calle 123"
  }
]