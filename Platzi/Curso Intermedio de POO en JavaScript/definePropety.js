const carlos = {
    name: 'carlito',
    age: 18,
    approvedCourses: ["Curso 1"],
    
    addCourse(newCourse) {
        console.log("This", this);
        console.log("This.approvedCourses", this.approvedCourses);
        this.approvedCourses.push(newCourse); // this hace referencia al objeto carlos
    },
};

// parte 1
// Object.defineProperty(juan, "navigator", {
//     value: "Chrome",
//     enumerable: false,
//     writable: true,
//     configurable: true,
// });

// Object.defineProperty(juan, "editor", {
//     value: "VSCode",
//     enumerable: true,
//     writable: false,
//     configurable: true
// });

// Object.defineProperty(juan, "terminal", {
//     value: "WSL",
//     enumerable: true,
//     writable: true,
//     configurable: false,
// });


// Object.defineProperty(juan, "pruebNasa", {
//     value: "marcianito",
//     enumerable: false,
//     writable: false,
//     configurable: false,
// });


// parte 2
Object.seal(carlos) // configurable se vuelve false
// Object.freeze(juan) // configurable y writable se vuelven false

console.log(Object.getOwnPropertyDescriptors(carlos));