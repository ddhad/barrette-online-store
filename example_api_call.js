fetch('http://0.0.0.0:8000/items/').then((data)=>{
         return data.json();
}).then((completeData)=>{

         completeData.map((data)=>{
                 console.log(data)

         });

}).catch((err)=>{
         console.log(err);
});