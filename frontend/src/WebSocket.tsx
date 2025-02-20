import { useState, useEffect } from 'react';
import { io } from "socket.io-client";

// const WEB_SOCKET_URL = "http://localhost:5000"
const WEB_SOCKET_URL = "ws://localhost:5000"
const socket = io("ws://localhost:5000");

const WebSocketComponent = () => {
    const [messages, setMessages] = useState([]);
    // const [isConnected, setIsConnected] = useState(false);

    socket.on("connect", () => {
        console.log("Connected to WebSocket server");
    });

    socket.on("disconnect", () => {
        console.log("Disconnected from WebSocket server");
    });

    socket.on("message", (message) => {
        console.log(`Received message: ${message}`);
        setMessages((prevMessages) => [...prevMessages, message]);
    });

    const lastMessage = messages[messages.length - 1]; // Get the last message
    const messageCount = messages.length; // Get the number of messages

    return (
        <div className="p-4 border rounded-lg shadow-md max-w-md mx-auto">
          <h2 className="text-xl font-semibold mb-2">WebSocket Messages</h2>
          <p>Number of messages received: {messageCount}</p>
          {lastMessage && <p><strong>Last message:</strong> {lastMessage}</p>}
        </div>
    );
};

export default WebSocketComponent;
