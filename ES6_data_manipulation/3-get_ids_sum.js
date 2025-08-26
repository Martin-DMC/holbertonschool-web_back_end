export default function getStudentIdsSum(lista) {
  if (!Array.isArray(lista)) {
    throw new TypeError('Lista must be a array');
  }
  const listaIds = lista.map((student) => student.id);
  const suma = listaIds.reduce((acumulador, valorActual) => {
    return acumulador + valorActual;
  }, 0);
  return suma;
}
