const fs = require('fs').promises;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8')
      .then((data) => {
        const lines = data.split('\n');
        const studentLines = lines.filter((line) => line.trim() !== '').slice(1);

        if (studentLines.length === 0) {
          console.log('Number of students: 0');
          resolve();
          return;
        }

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
        resolve();
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
