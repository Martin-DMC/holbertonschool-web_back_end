const http = require('http');
const countStudents = require('./3-read_file_async');

const DB_FILE = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    let responseText = 'This is the list of our students\n';

    const originalWrite = process.stdout.write;
    
    const capturedOutput = [];
    process.stdout.write = (chunk, encoding, callback) => {
      capturedOutput.push(chunk.toString());
      if (callback) {
        callback();
      }
    };

    try {
      await countStudents(DB_FILE);
      responseText += capturedOutput.join('');
      res.statusCode = 200;
    } catch (error) {
      responseText = `This is the list of our students\n${error.message}`;
      res.statusCode = 500;
    } finally {
      process.stdout.write = originalWrite;
      res.end(responseText);
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is running on http://localhost:1245');
});

module.exports = app;
