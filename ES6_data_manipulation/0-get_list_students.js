export default function getListStudents(
  id = undefined,
  firstName = undefined,
  location = undefined,
) {
  if (typeof id !== 'number' && id !== undefined) {
    throw new TypeError('id must be a number');
  }
  if (typeof firstName !== 'string' && firstName !== undefined) {
    throw new TypeError('firstName must be a string');
  }
  if (typeof location !== 'string' && location !== undefined) {
    throw new TypeError('location must be a string');
  }
  const listaStudents = [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];

  return listaStudents;
}
