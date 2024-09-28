const http = require('http');
const { countStudents } = require('./3-read_file_async'); // Ensure this path is correct

const app = http.createServer((req, res) => {
    const { url } = req;

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    if (url === '/') {
        res.end('Hello Holberton School!');
    } else if (url === '/students') {
        countStudents(process.argv[2])
            .then(() => {
                res.end('Done!');
            })
            .catch((error) => {
                res.statusCode = 500;
                res.end(error.message);
            });
    } else {
        res.statusCode = 404;
        res.end('Not Found');
    }
});

const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

module.exports = app;
