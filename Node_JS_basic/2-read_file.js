const fs = require('fs');

function countStudents(path) {
  try {
    const fileContent = fs.readFileSync(path, 'utf8');

    const lines = fileContent.split('\n');

    const studentLines = lines.filter((line) => line.trim() !== '').slice(1);

    const numberOfStudents = studentLines.length;
    console.log(`Number of students: ${numberOfStudents}`);

    const fields = {};
    studentLines.forEach((line) => {
      const [firstName, , , field] = line.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const count = fields[field].length;
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${count}. List: ${list}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
