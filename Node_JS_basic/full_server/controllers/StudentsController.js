import { readDatabase } from '../utils.js';

export class StudentsController {
    static async getAllStudents(req, res) {
        const dbName = req.app.get('dbName');
        try {
            const students = await readDatabase(dbName);
            const responseLines = ['This is the list of our students'];

            // Sort fields case-insensitively
            Object.keys(students)
                .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
                .forEach(field => {
                    responseLines.push(
                        `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`
                    );
                });

            res.status(200).send(responseLines.join('\n'));
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const dbName = req.app.get('dbName');
        const { major } = req.params;

        if (!['CS', 'SWE'].includes(major)) {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const students = await readDatabase(dbName);
            const studentList = students[major] || [];
            res.status(200).send(`List: ${studentList.join(', ')}`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}
