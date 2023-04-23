import { useState, useEffect } from "react";

function Booklist(){
    const[books, setBooks] = useState([])
    
    const displayBooks = () =>{
        return books.map(book =>
            <li>{book}</li>
            )
    }

    useEffect(() => {
        fetch("http://127.0.0.1:8000/apibook/")
        .then(response=>response.json())
        .then(data=>{
            setBooks(data.map(book=>book.title));
        })
        .catch(err=>console.log(err))
    })

    return(
        <ul>
            {displayBooks()}
        </ul>
    );
}

export default Booklist;