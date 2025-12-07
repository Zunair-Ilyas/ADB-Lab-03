const connectDB = require('../connect');

const updateMatch = async (req, res) => {
    try {
        const { id } = req.params;
        const updateData = req.body;

        const db = await connectDB();
        const collection = db.collection('cricket');

        const result = await collection.updateOne({ _id: id }, { $set: updateData });

        if (result.matchedCount === 0) {
            return res.status(404).json({ error: 'Match not found' });
        }

        res.status(200).json({ message: 'Match updated successfully' });
    } catch (error) {
        console.error('Error updating match:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

module.exports = updateMatch;