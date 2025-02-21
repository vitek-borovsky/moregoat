import { useState, useEffect } from 'react';
import { io } from "socket.io-client";

const WEB_SOCKET_URL = "ws://localhost:5000"
 // = io(WEB_SOCKET_URL);

class WebSocketService {
    private callback = null;
    private socket = null;
    private user_id = null;

    constructor() {
        this.socket = io(WEB_SOCKET_URL);

        this.socket.on("connect", () => {
            console.log("Connected to WebSocket server");
        });

        this.socket.on("disconnect", () => {
            console.log("Disconnected from WebSocket server");
        });

        this.socket.on("message", (message) => {
            console.log(`Received message: ${message}`);
        });

        this.socket.on("STONE_PLACED", (message) => {
            console.log(`Stone placed received ${message}`);
            const [ user, col, row ] = this.parseStonePlacedMessage(message);
            this.callback(user, col, row)
        });

        this.socket.on("REQUEST_ID", (id) => { // -1 if no Id available TODO
            console.log(`Id_recieved ${id}`);
            if (id == -1) return;
            this.user_id = id;
        });

        this.socket.emit("request_id")
    }

    subscribe(callback) {
        if (this.callback) return;
        this.callback = callback
    }

    parseStonePlacedMessage(input) {
        const regex = /^([^@]+)@([^x]+)x(.+)$/;
        const match = input.match(regex);

        if (match) {
            const [, user, col, row] = match;
            return [ user, Number(col), Number(row) ];
        }
        throw new Error("Invalid format");
    }

    // Improvement: rewrite this to json
    place_stone = (col, row) => {
        this.socket.emit("stone_placed", `${this.user_id}@${col}x${row}`)
    }
}

export default WebSocketService
