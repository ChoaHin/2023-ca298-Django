import { useState } from "react";

function CounterComponent(){
	const [counter, setCounter] = useState(0);
	// const [stringVar, setStringVar] = useState("Hi"); // string
	// const [objVar, setObjVar] = useState({'type':'initial'}) // json object
	// const [arrVar, setArrVar] = useState([1,2,3]); // array

    // the rest of the component
    return(
        <div>
            <p>{counter}</p>
            <button onClick={
                ()=>{
                    setCounter(counter + 1)
                }
            }>Add Counter</button>
        </div>
    )
}

export default CounterComponent