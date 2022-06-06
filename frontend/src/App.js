import './App.css';
import MainPanel from './mainpanel/mainpanel';
import NavPanel from './navpanel/navpanel';
import Services from './services';
import React, { useEffect, useState } from 'react';

export const NodeContext = React.createContext()

function App() {
    const [url, setURL] = useState(Services.generateURL("root"))
    const [nodes, setNodes] = useState(null)
    const [loading, setLoading] = useState(true)
    function navigateChild(value) {
        setURL(`${url}${value}/`);
        console.log(url);
    }
    function navigateParent(value){
        let cleanValue = value.substring(0, value.indexOf(" "));
        if(cleanValue !== "root"){
            let updatedUrl = url.substring(0, url.indexOf(cleanValue) + cleanValue.length + 1)
            setURL(updatedUrl)
        }
        else{
            setURL(Services.generateURL("root"))
        }
        console.log(url)
    }

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
                    <NavPanel navigateParent={navigateParent} />
                    <MainPanel navigateChild={navigateChild}/>
                </>)
            : <div>Data loading</div>}
        </NodeContext.Provider>
    );
}

export default App;
