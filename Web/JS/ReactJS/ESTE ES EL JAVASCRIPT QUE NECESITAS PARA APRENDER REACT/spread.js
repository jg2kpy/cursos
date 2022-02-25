const array = [1,2,3,4,5]
const otroArray = [6,7,8,9,10]

const nuevoArray = [...array,...otroArray]
console.log(nuevoArray);

const obj1 = {
    a: 'a',
    b: 'b',
    c: 'c',
}

const obj2 = {
    d: 'd',
    e: 'e',
    f: 'f',
}

const ob3 = {...obj1, ...obj2}