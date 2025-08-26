export default function getListStudentIds(lista) {
  if (!Array.isArray(lista)) {
    return [];
  }
  return lista.map((student) => student.id);
}
