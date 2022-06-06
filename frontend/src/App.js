import './App.css';
import MainPanel from './mainpanel/mainpanel';
import NavPanel from './navpanel/navpanel';
import Services from './services';
import React, { useEffect, useState } from 'react';

export const NodeContext = React.createContext()

function App() {
    const url = Services.generateURL("root")
    const [nodes, setNodes] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        async function fetchData() {
            const response = await fetch(url);
            const data = await response.json();
            setNodes(data);
            setLoading(false);
        }
        fetchData();
    }, [url]);
    
    return (
        <NodeContext.Provider value={nodes}>
            {!loading ? (<>
                    <NavPanel />
                    <MainPanel />
                </>)
            : <div>Data loading</div>}
        </NodeContext.Provider>
    );
}

export default App;
