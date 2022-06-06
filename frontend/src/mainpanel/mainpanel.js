import React, { useContext } from 'react';
import { NodeContext } from '../App';

const MainPanel = ({ navigateChild }) => {
    const nodes = useContext(NodeContext);
    return (
        <>{
            nodes.file ? (<span>This is file: {nodes.file}</span>) : (<ul>
                {
                    nodes.children.map((value, index) => (
                        <li key={index} onClick={(e) => navigateChild(e.target.innerText)}>{value.name}</li>
                    ))
                }
            </ul>)
        }</>
        
    )
}

export default MainPanel