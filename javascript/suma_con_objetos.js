function sumaConKwargs(kwargs) {
    let resultado = 0;
    for (let key in kwargs) {
      if (kwargs.hasOwnProperty(key)) {
        resultado += kwargs[key];
      }
    }
    return resultado;
  }
  
  const valores = {
    num1: 10,
    num2: 20,
    num3: 30
  };
  
  const resultado = sumaConKwargs(valores);
  console.log(`La suma es: ${resultado}`);
  