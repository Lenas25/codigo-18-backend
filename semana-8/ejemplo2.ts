
// function manufacture(gifts : string[], materials:string){
//   const giftsManufactured:string[] = [];

//   // Iteramos sobre cada regalo
//   for (let gift of gifts){
//     let isPosible: boolean = true;

//     // Iteramos sobre cada caracter del regalo
//     gift.split('').forEach(character => {
//       // Si el material no contiene el caracter
//       if(!materials.includes(character)){
//         isPosible = false;
//       }
//     })

//     // Si es posible fabricar el regalo
//     if(isPosible){
//       giftsManufactured.push(gift);
//     }
//   }

//   return giftsManufactured;
// }


function manufacture(gifts: string[], materials: string){
  const materialesSet = new Set(materials);
  const giftsManufactured:string[] = [];

  for (let gift of gifts){
    // primero el gift se vuelve array y luego con every se iteran todos los elementos verificando si cada caracter esta en el set de materiales
    if(gift.split('').every(character => materialesSet.has(character))){
      giftsManufactured.push(gift);
    }
  }
  
  return giftsManufactured;
}

const gifts = ['tren','oso','pelota'];
const materials = 'tronesa';
console.log(manufacture(gifts, materials))