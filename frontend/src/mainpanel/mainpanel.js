import React, { useContext } from 'react';
import { NodeContext } from '../App';

const MainPanel = () => {
    const nodes = useContext(NodeContext);

    return (
        <ul>
            {
                nodes.children.map((value, index) => (
                    <li>{value.name}</li>
                ))
            }
        </ul>
    )
}

export default MainPanel