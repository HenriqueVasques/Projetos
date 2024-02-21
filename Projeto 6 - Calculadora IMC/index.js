const form = document.getElementById('form');

form.addEventListener('submit', function(event){
    event.preventDefault();

 

    const height = document.getElementById('height').value;
    const weight = documet.getElementById('weight').value;

 
    const bmi = weight / (height * height).toFixed(2); 

    const value = document.getElementById('value');
    let description ='';
    
    document.getElementById('infos').classList.remove('hide');
    document.getElementById('resultado').classList.remove('resultado');
   
    


   
    if(bmi < 18.5){
        description = 'Cuidado! Você está abaixo do peso!'
    }
        value.textContent = bmi
        document.getElementById('description').textContent = description
});

