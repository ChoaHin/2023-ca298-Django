import { useState, useEffect } from "react";

function Book({id}){
    const [book, setBook] = useState([]) //initial state for testing
    const [isLoaded, setIsLoaded] = useState(false);

    const displayBook = () =>{
        return book.map(elem=>
            <div>
                <h1>{elem.title}</h1>
                <li>{elem.author}</li>
                <li>{elem.year}</li>
                <li>{elem.genre}</li>
            </div>

        )
    }

    useEffect(()=>{
        //our code goes here
        fetch(`http://127.0.0.1:8000/apibook/${id}/`)
        .then(response=>response.json())
        .then(data=>{
            setBook([data]) //get the array of text out and set it as our state
            setIsLoaded(true);
        })
        .catch(err=>console.log(err))
    }
    )

    if(isLoaded){
        return (
            <ul>
                {displayBook()}
            </ul>
        )
    }
    else{
        return (
            <p>
                404 book not found
            </p>
        )
    }
}

export default Book