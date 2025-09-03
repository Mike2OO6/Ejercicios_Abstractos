function contadornew() {
    let valor = 20000000;

    return{
        incrementar: function () {
            valor++;
        },
        decrementar: function(){
         valor--;
        },
            obtenerValor: function(){
                return valor;
            }
        }
    };  

    
 const contador = contadornew();
contador.incrementar();
contador.incrementar();
console.log(contador.obtenerValor());

contador.decrementar();
console.log(contador.obtenerValor());


    
