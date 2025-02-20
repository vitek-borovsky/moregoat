import { useEffect, useState } from "react";
import WebSocketComponent from  './WebSocket.tsx'
import BoardComponent from './Board.tsx'
import './App.css'

function App() {
  const [data, setData] = useState(null)

      // <WebSocketComponent/>
  return (
    <>
      <h1>Hi</h1>
      <div className="flex justify-center items-center min-h-screen bg-gray-900">
        <BoardComponent boardSize={5} />
      </div>
    </>
  )
  // {data ? <p>{data.title}</p> : <p>Loading...</p>}
}



export default App
