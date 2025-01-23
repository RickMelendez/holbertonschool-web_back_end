const http = require('http');

const port = 1245;

// create a server object
const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('Hello Holberton School!'); // write a response to the client
  res.end(); // end the response
});
app.listen(port);
module.exports = app;
