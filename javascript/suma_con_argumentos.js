function sumaConArgs(...args) {
    let resultado = 0;
    for (let numero of args) {
      resultado += numero;
    }
    return resultado;
  }
  
  const numeros = [1, 2, 3, 4, 5];
  const resultado = sumaConArgs(...numeros);
  console.log(`La suma es: ${resultado}`);
  