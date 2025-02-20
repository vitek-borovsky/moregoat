import { useState, useEffect } from 'react';
import { io } from "socket.io-client";

const WEB_SOCKET_URL = "ws://localhost:5000"
const socket = io("ws://localhost:5000");

// const WebSocketComponent = () => {
//     const [messages, setMessages] = useState([]);
//     // const [isConnected, setIsConnected] = useState(false);
//
socket.on("connect", () => {
    console.log("Connected to WebSocket server");
});

socket.on("disconnect", () => {
    console.log("Disconnected from WebSocket server");
});

socket.on("message", (message) => {
    console.log(`Received message: ${message}`);
});

socket.on("ACK-testing", (message) => {
    console.log(`Received ACK`);
});

// Improvement: rewrite this to json
const place_stone = (col, row) => {
    socket.emit("stone_placed", `${col}x${row}`)
}

export default place_stone

