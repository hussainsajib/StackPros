import React, { useContext } from 'react'
import BreadCrumb from '../breadcrumb/breadcrumb'
import { NodeContext } from '../App'

const NavPanel = () => {
    const nodes = useContext(NodeContext)
    let curNode = nodes.current
    const result = []
    while (true){
        result.unshift(curNode.name);
        if(curNode.parent != null){
            curNode = curNode.parent;
        }
        else{
            break;
        }
        
    }
    return (
        <div>{result.map(item => <BreadCrumb currentNode={item} />)}</div>
    )
}

export default NavPanel