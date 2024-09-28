const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n').filter(line => line.trim() !== '');
            if (lines.length === 0) {
                reject(new Error('Cannot load the database'));
                return;
            }

            console.log(`Number of students: ${lines.length - 1}`);

            const fields = {};
            lines.slice(1).forEach(line => {
                const [firstname, , , field] = line.split(',');
                if (!fields[field]) fields[field] = [];
                fields[field].push(firstname);
            });

            Object.keys(fields).forEach(field => {
                console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
            });

            resolve();
        });
    });
}

module.exports = { countStudents };
