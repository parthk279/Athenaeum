import React, { useState } from "react";
import "./SearchBar.css";

function SearchBar({ placeholder, data }) {
  
  const[filterData, setFilterData] = useState([]);
  
  const handleFilter = (event) =>{
    const searchWord = event.target.value
    const newFilter = data.filter((value)=>{
        return value.title.toLowerCase().includes(searchWord.toLowerCase());
    });

    if(searchWord == ""){
        setFilterData([])
    }
    else{
        setFilterData(newFilter);
    }    
  };

  return (
    <div className="search">
      <div className="searchInputs">
        <input
          type="text"
          placeholder={placeholder}
          onChange={handleFilter}
        />
        <div className="searchIcon">   
        </div>
      </div>
      {filterData.length != 0 && ( 
        <div className="dataResult" >
            {filterData.slice(0,15).map((value,key)=>{
                return(
                    <a className="dataitem" href={value.link} target="_blank" >
                    <p>{value.title}</p>
                    </a>
                );
            })}
        </div>
       )}
    </div>
  );
}    

export default SearchBar;
