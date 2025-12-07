const express = require('express');
const app = express();
const cors = require('cors');
require('dotenv').config();
const port = process.env.PORT || 3000;
const connectDB = require('./connect');
const routes = require('./route');

app.use(express.json());
app.use(cors());
app.use('/', routes);

const start = () => {
    connectDB();
    app.listen(port, () => {
        console.log(`Server running on ${port}...`);
    })
}

start();