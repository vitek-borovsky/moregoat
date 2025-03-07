import { useEffect } from 'react';
import { io } from "socket.io-client";

const WEB_SOCKET_URL = "ws://localhost:5000"

class WebSocketService {
    private socket = io(WEB_SOCKET_URL);
    private join_game_callback = null;

    private game_id = null;
    private player_id = null;

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

        this.socket.on("JOIN_GAME", (payload) => {
            console.log(`Joined Game(${payload})`)

            const data = JSON.parse(payload);
            this.game_id = data.game_id;
            this.player_id = data.player_id;
            this.join_game_callback(data.player_id, data.board_size, data.player_count);
        });
    }

    subscribe_join_game_callback = (callback) => {
        this.join_game_callback = callback;
        console.log("join_game_callback subscribed");
    }

    // TODO add functionality to check socket is still valid
    createGame = (board_size, player_count) => {
        console.log(`Game created player_count=${player_count} board_size=${board_size}`);
        const data = {
            "player_count" : player_count,
            "board_size" : board_size
        };
        this.socket.emit("create_game", JSON.stringify(data));
    }

    join_game = (game_id) => {
        console.log(`Joined game ${game_id}`);
        this.socket.emit("join_game", `${game_id}`);
    }

    sendEcho = () => {
        this.socket.emit("ping", "HELLO");
    }

    placeStone = (col: number, row: number) => {
        const data = {
            "game_id" : this.game_id,
            "player_id" : this.player_id,
            "col" : col,
            "row" : row
        };
        this.socket.emit("stone_placed", JSON.stringify(data));
    }
}


export default WebSocketService
