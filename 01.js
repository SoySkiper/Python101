const squareList = arr => {
  // Cambia solo el código debajo de esta línea
  const enteros = arr.filter( e => typeof e === 'number' && e % 1 === 0);
  const quat = enteros.map( e => e * e);
  return quat;
  // Cambia solo el código encima de esta línea
};

const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);