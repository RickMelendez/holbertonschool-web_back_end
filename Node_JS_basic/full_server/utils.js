import fs from 'fs/promises';

export const readDatabase = async (filePath) => {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.trim().split('\n');
        const students = {};

        lines.forEach(line => {
            const [firstName, major] = line.split(',');
            if (firstName && major) {
                if (!students[major]) {
                    students[major] = [];
                }
                students[major].push(firstName);
            }
        });

        return students;
    } catch (error) {
        throw error; // Reject with error if file cannot be read
    }
};
