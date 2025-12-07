const connectDB = require('../connect');

const filterByLocation = async (req, res) => {
    try {
        const { location } = req.params;

        const db = await connectDB();
        const collection = db.collection('cricket');
        const results = await collection.find({ Location: location }).toArray();
        res.status(200).json(results);
    } catch (error) {
        console.error('Error filtering matches by location:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

module.exports = filterByLocation;