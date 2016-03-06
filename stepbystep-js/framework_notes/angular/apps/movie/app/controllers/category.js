/**
 * Created by patrick on 15/8/9.
 */
var mongoose = require('mongoose');
var Category = mongoose.model('Category');

exports.new=function(rq,res){
  res.render(category_admin),{
    title:'imooc backend category',
    category:{}
  };
};

exports.save =function(req,res){
  var _category=req.body.category
  var category=new Category(_category)
  category.save(function(err,category){
    if(err){
      console.log(err)
    }

    res.redirect('admin/category/list');
  });
}

exports.list=function(req,res){
  Category.fetch(function(err,categories){
    if(err){
      console.log(err)
    }
    res.render('categorylist',{
      title: 'imooc list',
      categories:categories
    })
  });
}
