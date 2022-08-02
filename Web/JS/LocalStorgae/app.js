function obtener_localstorage(){

    if(localStorage.getItem('nombre')){
        let nombre = localStorage.getItem('nombre');
        let persona = JSON.parse(localStorage.getItem('persona'));
    
        console.log(nombre);
        console.log(persona);
    }else{
        console.log("No hay entradas en el localstorage");
    }
}


function guardar_localstorage(){

    let persona = {
        nombre: 'Junior',
        edad: 21 ,
        correo: 'xyz@xyz.com',
        coords: {
            lat: 10,
            lng: -10
        }
    }

    let nombre = 'Jose'

    localStorage.setItem('nombre',nombre);
    localStorage.setItem('persona',JSON.stringify(persona));

};

//guardar_localstorage();
obtener_localstorage();