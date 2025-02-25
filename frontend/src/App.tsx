import { useEffect } from 'react';
import WebSocketService from './WebSocketService.tsx'
import Board from './Board.tsx'
import './App.css'

function App() {
  const wss = new WebSocketService()
  return (
    <>
        <div>
            <h1>Hello World</h1>
            <button onClick={wss.sendEcho}>Send Echo</button>
        </div>
        <Board boardSize={5} />
    </>
  );
}

export default App
