import { io } from "socket.io-client";

const WEB_SOCKET_URL = "ws://localhost:5000"

class WebSocketService {
    private socket = io(WEB_SOCKET_URL);

    private join_game_callback: ((playerId: number, boardSize: number) => void) | null = null;

    private game_id: string | null = null;
    private player_id: number | null = null;
    private player_count: number | null = null;

    getGameId = () => this.game_id;
    getPlayerId = () => this.player_id;
    getPlayerCount = () => this.player_count;

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
            this.player_count = data.player_count;

            this.join_game_callback!(data.player_id, data.board_size);
        });

        this.socket.on("STONE_PLACED", (payload) => {
            console.log(`STONE_PLACED (${payload})`)
        });
    }

    subscribe_join_game_callback = (callback: (player_id: number, board_size: number) => void) => {
        this.join_game_callback = callback;
        console.log("join_game_callback subscribed");
    }

    // TODO add functionality to check socket is still valid
    createGame = (board_size: number, player_count: number) => {
        console.log(`Game created player_count=${player_count} board_size=${board_size}`);
        const data = {
            "player_count" : player_count,
            "board_size" : board_size
        };
        this.socket.emit("create_game", JSON.stringify(data));
    }

    joinGame = (game_id: string) => {
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
