const http = require('http');

const app = http.createServer((req, res) => {
    res.statusCode = 200;  // Set the status code to 200 (OK)
    res.setHeader('Content-Type', 'text/plain');  // Set the response content type to plain text
    res.end('Hello Holberton School!');  // Send the response and close the connection
});

const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
