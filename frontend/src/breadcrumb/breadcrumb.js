import React from 'react'
import Services from '../services'

const BreadCrumb = ({ currentNode, navigateParent }) => {
    return (
        <span onClick={(e)=> navigateParent(e.target.innerText) } className="breadcrumb">{currentNode} / </span>
    )
}

export default BreadCrumb