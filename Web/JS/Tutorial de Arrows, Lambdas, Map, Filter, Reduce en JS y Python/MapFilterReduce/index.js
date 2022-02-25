function apply(num, f) {
    return f(num)
}

function double(num) {
    return 2 * num
}

//console.log(apply(5, (num) => 2 * num))

const dollars = ["32$", "15$", "12$", "17$", "20$"]

//Map

//Forma boomer
let prices = []
for (let i=0; i < dollars.length; i++){
    prices[i] = Number(dollars[i].slice(0,dollars[i].length - 1))
}

//Forma zoomer
prices = []
for(const dollar of dollars){
    prices.push(Number(dollar.slice(0,dollar.length - 1)))
}

//Forma hacker 2022
prices = []
prices = dollars.map((dollar) =>  Number(dollar.slice(0,dollar.length - 1)))

console.log(prices);

//Filter

//Forma zoomer
let expensive = []
for(const price of prices){
    if(price >= 20){
        expensive.push(price)
    }
}
console.log(expensive);

//Forma hacker 2022
expensive = prices.filter((price) => price >= 20)
console.log(expensive);

//Reduce
//Forma zoomer
let sum = 0
for (price of expensive){
    sum += price
}
console.log(sum);

//Forma hacker 2022
sum = expensive.reduce((acum, price) => acum + price)
console.log(sum);

//De una

sum = dollars
    .map(dollar =>  Number(dollar.slice(0,dollar.length - 1)))
    .filter(price => price >= 20)
    .reduce((acum, price) => acum + price)

console.log(sum);

sum = 0
for(const dollar of dollars){
    const price = Number(dollar.slice(0,dollar.length - 1))
    if (price >= 20){
        sum += price
    }
}

console.log(prices.map(price => ({price, currency: '$'})).forEach(obj => obj.price += 10))