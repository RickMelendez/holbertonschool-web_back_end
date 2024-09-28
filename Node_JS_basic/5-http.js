const http = require('http');
const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
            if (err) return reject(new Error('Cannot load the database'));

            const lines = data.split('\n').slice(1, -1); // skip header and last empty line
            const header = data.split('\n')[0].split(','); // get header line
            const idxFn = header.indexOf('firstname');
            const idxFd = header.indexOf('field');
            const fields = {};
            const students = {};
            const all = {};

            lines.forEach((line) => {
                const list = line.split(',');
                if (!fields[list[idxFd]]) fields[list[idxFd]] = 0;
                fields[list[idxFd]] += 1;
                if (!students[list[idxFd]]) students[list[idxFd]] = '';
                students[list[idxFd]] += students[list[idxFd]] 
                    ? `, ${list[idxFn]}` 
                    : list[idxFn];
            });

            all.numberStudents = `Number of students: ${lines.length}\n`;
            all.listStudents = [];
            for (const key in fields) {
                if (Object.prototype.hasOwnProperty.call(fields, key)) {
                    const element = fields[key];
                    all.listStudents.push(`Number of students in ${key}: ${element}. List: ${students[key]}`);
                }
            }
            resolve(all);
        });
    });
}

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/') {
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        res.write('This is the list of our students\n');
        countStudents(process.argv[2])
            .then((data) => {
                res.write(data.numberStudents);
                res.write(data.listStudents.join('\n'));
                res.end();
            })
            .catch((err) => {
                res.statusCode = 500; // Internal Server Error
                res.end(err.message);
            });
    } else {
        res.statusCode = 404; // Not Found
        res.end('404 Not Found');
    }
});

app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
