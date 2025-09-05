async function run() {
  if (process.stdin.isTTY) {
  process.stdout.write('Welcome to Holberton School, what is your name?\n');
  }

  for await (const chunk of process.stdin) {
    const name = chunk.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`)
    if (process.stdin.isTTY) {
      process.exit();
    }
  }

  process.stdout.write('This important software is now closing\n');
}

run();
