var username = 'Nicolas';
var suma = function (a, b) {
    return a + b;
};
suma(1, 3);
var Person = /** @class */ (function () {
    function Person(age, lastName) {
        this.age = age;
        this.lastName = lastName;
    }
    return Person;
}());
var nico = new Person(15, 'Gutierrez');
