function myFunction() {
    var palabra = document.getElementById("num").value;
    var letras;
    var palabra2 = document.getElementById("nom").value;
    var letras2;
    var palabra3 = document.getElementById("pai").value;
    var letras3;
    var palabra4 = document.getElementById("tel").value;
    var letras4;
    letras = palabra.substr(0,2);
    letras2 = palabra2.substr(0,2);
    letras3 = palabra3.substr(-2);
    letras4 = palabra4.substr(-2);  
    document.getElementById("con").value = letras + "" + letras2.toUpperCase() + "" + letras3.toLowerCase() + "" + letras4;
}

//Lo que hace esta función es obtener las id de numero id, nombre, pais y telefono y las declara en una variable, luego
//hace los substring correspondiente ya sea obtener los 2 primeros o los 2 ultimos y las declara en otras variables, 
//luego obtiene la id de la contraseña y le asigna como valor las variables obtenidas con los substr todas juntas, además que
//algunas las convierte en mayusculas o minusculas, esta función es llamada en un evento onkeyup que esta en el form, haciendo
//que cuando uno rellene el textinput de nombre, id, pais, telefono vaya enviando el resultado el valor que se le asigno a la
//contraseña, en otras palabras cuando uno va rellenando nombre, pais, id, telefono se va generando la contraseña automaticamente
//también el formulario la contraseña tiene un readonly, para que de esta forma no se altere la contraseña generada
