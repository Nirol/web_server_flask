import React, { Component, useState, useEffect } from 'react';


const CounterAppHook = () => {

    const [count, setCount] = useState(0)


useEffect( () => {

    document.title = 'Clicked ${(count} times';

});

   const  increment = () => {


        setCount(count +1);
    };


return ( 
    <div>
    <h1>Counter app</h1>
    <button onClick={increment}> Clicked {count} times</button>    
    
    </div>    


    
    
    );

};

export default CounterAppHook;