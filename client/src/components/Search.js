import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function Search() {

  const [term, setTerm] = useState('')
  const [nonprofits, setNonprofits] = useState([])

  const baseUrl = 'http://localhost:8080'


  const handleClick = async () => {
    try {
      const res = await (await axios.get(`${baseUrl}/search/${term}`)).data.nonprofits
      setNonprofits(res)
    }
    catch (er) {
      console.log(er)
    }
  }

  return (
    <div>
      <div>
        <input placeholder='search for nonprofit' type='text' name='term' value={term} onChange={(ev) => setTerm(ev.target.value)} />
        <button type='click' onClick={() => handleClick()}>Go</button>
      </div>
      <ul>
        {
          nonprofits.map(org => {
            return(
              <div key={org.ein}>
                <img src={org.logoUrl} />
                {org.name}
              </div>
            )
          })
        }
      </ul>
    </div>
  )
}
