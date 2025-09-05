const readline = require('readline');

if (process.stdin.isTTY) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question('Welcome to Holberton School, what is your name?\n', (answer) => {
    process.stdout.write(`Your name is: ${answer}\n`);
    
    rl.close();
  });
} else {
  let inputData = '';
  process.stdin.on('data', (chunk) => {
    inputData += chunk.toString();
  });
  process.stdin.on('end', () => {
    const name = inputData.trim();

    process.stdout.write(`Your name is: ${name}\n`);

    process.stdout.write('This important software is now closing\n');
  });
}
