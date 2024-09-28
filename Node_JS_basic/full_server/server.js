// full_server/server.js
import express from 'express';
import routes from './routes/index.js';

const app = express();
const port = 1245;

// Middleware to set the database name from command-line argument
app.use((req, res, next) => {
    app.set('dbName', process.argv[2]);
    next();
});

// Use the defined routes
app.use(routes);

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

// Export the app
export default app;
