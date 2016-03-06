/**
 * Created by patrick on 15/8/9.
 */
var mongoose = require('mongoose')
var CategorySchema = require('../schemas/category')
var Category = mongoose.model('Category', CategorySchema)

module.exports = Category
