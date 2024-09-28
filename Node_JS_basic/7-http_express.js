// 7-http_express.js
const express = require('express');
const fs = require('fs');
const app = express();
const port = 1245;

// Helper function to read CSV file and return student data
function readStudentData(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return;
            }
            const lines = data.trim().split('\n');
            const students = lines.map(line => {
                const [name, course] = line.split(',');
                return { name, course };
            }).filter(student => student.name && student.course); // Filter out invalid students
            resolve(students);
        });
    });
}

// Route for root path
app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Route for /students path
app.get('/students', async (req, res) => {
    const dbName = process.argv[2];
    if (!dbName) {
        res.status(400).send('Database file not specified');
        return;
    }

    try {
        const students = await readStudentData(dbName);
        const csStudents = students.filter(student => student.course === 'CS');
        const sweStudents = students.filter(student => student.course === 'SWE');
        
        const response = [
            'This is the list of our students',
            `Number of students: ${students.length}`,
            `Number of students in CS: ${csStudents.length}. List: ${csStudents.map(s => s.name).join(', ')}`,
            `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.map(s => s.name).join(', ')}`
        ].join('\n');
        
        res.send(response);
    } catch (error) {
        res.status(500).send('Error reading the database file');
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

// Export the app
module.exports = app;
