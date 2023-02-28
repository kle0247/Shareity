import React, { useState, useEffect } from 'react'

export default function Search() {

  const [term, setTerm] = useState('')
  
  const handleClick = () => {
    //axios call to get search orgs - using in term
    console.log('clicked from function')
  }

  return (
    <div>
      <input placeholder='search for nonprofit' type='text' name='term' value={term} onChange={(ev) => setTerm(ev.target.value)}/>
      <button type='click' onClick={ () => handleClick() }>Go</button>
    </div>
  )
}
