import { useEffect } from 'react';
import { io } from "socket.io-client";

const WEB_SOCKET_URL = "ws://localhost:5000";

class WebSocketService {
    private socket = io(WEB_SOCKET_URL);

    constructor() {
        this.socket.on("connect", () => {
            console.log("Connected to backend");
        });

        this.socket.on("disconnect", () => {
            console.log("Disconnected to backend");
        });

        this.socket.on("PING", (payload) => {
            console.log(`PING recieved ${payload}`);
        });

        this.socket.on("JOIN_GAME", (game_id) => {
            console.log(`Game ${game_id} started`)
        });
    }

    sendEcho = () => {
        if (!this.socket) {
            console.log("Cannot send Hello: Socket in invalid-state");
            return;
        }
        this.socket.emit("ping", "HELLO");
    }
}


export default WebSocketService
