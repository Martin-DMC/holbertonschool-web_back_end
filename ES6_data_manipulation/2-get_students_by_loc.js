export default function getStudentsByLocation(lista, city) {
  if (!Array.isArray(lista)) {
    throw new TypeError('Lista must be a array');
  }
  if (typeof city !== 'string') {
    throw new TypeError('city must be a string');
  }
  return lista.filter((student) => student.location === city);
}
