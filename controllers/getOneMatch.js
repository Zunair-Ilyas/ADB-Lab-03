const connectDB = require('../connect');

const getOneMatch = async(req, res) => {
    try {
        const {id} = req.params;
        const db = await connectDB();
        const collection = db.collection('cricket');
        const match = await collection.findOne({ _id: id });
        if (!match) {
            return res.status(404).json({ error: 'Match not found' });
        }
        res.status(200).json(match);
    } catch (error) {
        console.error('Error retrieving match:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

module.exports = getOneMatch;