import React, { useContext } from 'react';
import { NodeContext } from '../App';

const MainPanel = ({ navigateChild }) => {
    const nodes = useContext(NodeContext);
    return (
        <div className='mainpanel'>{
            nodes.file ? (<span className='mainpanelfile'>This is file: {nodes.file}</span>) : (<ul>
                {
                    nodes.children.map((value, index) => (
                        <li key={index} onClick={(e) => navigateChild(e.target.innerText)} className="mainpanelitem">{value.name}</li>
                    ))
                }
            </ul>)
        }</div>
        
    )
}

export default MainPanel