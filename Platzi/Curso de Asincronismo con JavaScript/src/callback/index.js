function sum(num1, num2) {
    return num1 + num2;
}

function rest(num1, num2) {
    return num1 - num2;
}

function mult(num1, num2) {
    return num1 * num2;
}

function div(num1, num2) {
    return num1 / num2;
}

function calc(num1, num2, callback) {
    return callback(num1, num2);
};

console.log(calc(3,4,div));

setTimeout(function () {
        console.log('Hola JS');
}, 5000)

function gretting(name) {
    console.log(`Hola ${name}`)
}

setTimeout(gretting, 2000, 'Junior')