/**
 * Created by patrick on 15/9/2.
 */

var language = {
    name: 'javascript',
    isSupportedByBrowsers: true,
    createdIn: 1995,
    author: {
        firstName: 'Brendan',
        lastName: 'Eich'
    },
    getAuthorFullName: function () {
        return this.author.firstName + " " + this.author.lastName;
    }
};


var variable = language.name;
// variable now contains "JavaScript" string.
variable = language['name'];
// The lines above do the same thing. The difference is that the second one lets you use litteraly any string as a property name, but it's less readable.
variable = language.newProperty;
// variable is now undefined, because we have not assigned this property yet.
language.newProperty = 'new value';
// Now the object has a new property. If the property already exists, its value will be replaced.
language['newProperty'] = 'changed value';
// Once again, you can access properties both ways. The first one (dot notation) is recomended.
console.log(language)