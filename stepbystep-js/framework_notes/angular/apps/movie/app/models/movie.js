/**
 * Created by patrick on 15/8/9.
 */
var mongoose = require('mongoose')
var MovieSchema = require('../schemas/movie')
var Movie = mongoose.model('Movie', MovieSchema)

module.exports = Movie
