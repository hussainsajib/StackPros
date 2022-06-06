import React from 'react'
import Services from '../services'

const BreadCrumb = ({ currentNode }) => {
    return (
        <span onClick={()=>console.log("Clicked")}>{currentNode} / </span>
    )
}

export default BreadCrumb