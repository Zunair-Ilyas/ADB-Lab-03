const express = require('express');
const router = express.Router();
const getAllMatches = require('./controllers/getAllMatches');
const getOneMatch = require('./controllers/getOneMatch');
const createMatch = require('./controllers/createMatch');
const updateMatch = require('./controllers/updateMatch');
const deleteMatch = require('./controllers/deleteMatch');
const filterData = require('./controllers/filterByLocation');

router.route('/matches').get(getAllMatches);
router.route('/matches/:id').get(getOneMatch);
router.route('/matches').post(createMatch);
router.route('/matches/:id').put(updateMatch);
router.route('/matches/:id').delete(deleteMatch);
router.route('/matches/location/:location').get(filterData);

module.exports = router;