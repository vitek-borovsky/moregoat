import { useEffect } from 'react';
import { io } from "socket.io-client";
import './App.css'

const WEB_SOCKET_URL = "ws://localhost:5000";

function App() {
  let socket = null;
  const sendEcho = () => {
      if (!socket) {
          console.log("Cannot send Hello: Socket in invalid-state")
          return
      }

      socket.emit("ping", "HELLO");
  }

  useEffect(() => {
      socket = io(WEB_SOCKET_URL);
      socket.on("connect", () => {
          console.log("Connected to backend");
      });

      socket.on("disconnect", () => {
          console.log("Disconnected to backend");
      });

      socket.on("PING", (payload) => {
          console.log(`PING recieved ${payload}`);
      });
  }, []);


  return (
    <>
        <h1>Hello World</h1>
        <button onClick={sendEcho}>Send Echo</button>
    </>
  )
}

export default App
