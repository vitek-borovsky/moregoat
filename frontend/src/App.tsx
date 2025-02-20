import { useEffect, useState } from "react";
import WebSocketComponent from  './WebSocket.tsx'
import './App.css'

function App() {
  const [data, setData] = useState(null)

  return (
    <>
      <h1>Hi</h1>
      <WebSocketComponent/>
    </>
  )
  // {data ? <p>{data.title}</p> : <p>Loading...</p>}
}



export default App
