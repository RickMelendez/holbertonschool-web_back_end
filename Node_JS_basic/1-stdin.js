// Display the welcome message
console.log("Welcome to Holberton School, what is your name?");

// Listen for user input
process.stdin.on('data', (data) => {
  // Trim the input to remove any extra newline or spaces
  const name = data.toString().trim();
  
  // Display the user's name
  console.log(`Your name is: ${name}`);
  
  // Exit the process
  process.exit();
});

// Listen for process exit event to display the closing message
process.on('exit', () => {
  console.log("This important software is now closing");
});
