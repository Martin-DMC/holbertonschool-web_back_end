export default function updateStudentGradeByCity(lista, city, newGrades) {
  if (!Array.isArray(lista)) {
    throw new TypeError('Lista must be a array');
  }
  if (!Array.isArray(newGrades) && newGrades !== undefined) {
    throw new TypeError('newGrades must be a array');
  }
  if (typeof city !== 'string') {
    throw new TypeError('City must be a string');
  }
  return lista
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.find((gradeObj) => gradeObj.studentId === student.id);
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
