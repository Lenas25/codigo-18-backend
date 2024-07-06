// como tipado implicito
// que TS interpreta el tipo de dato basado en valor
let nombre = "Elena" //string

// tipado explicito
let direccion: string = "av mi casa 123"

const numero1: number = 100
const alumnos: object = []

function sumar(n1:number, n2:number){
    return n1+n2;
}

console.log(sumar(10,20))

const sumaDeLosProductosDeHoy: number = 100;