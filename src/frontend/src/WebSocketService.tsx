import { io } from "socket.io-client";

const WEB_SOCKET_URL = "ws://localhost:5000"

class WebSocketService {
    private socket = io(WEB_SOCKET_URL);

    private joinGameCallback: ((boardSize: number) => void) | null = null;
    private stonePlacedCallback: ((col: number, row: number, player_id: number) => void) | null = null;
    private stoneCapturedCallback: ((stones: number[][]) => void) | null = null;
    private updatePointsCallback: ((points: number[]) => void) | null = null;
    private playerPassCallback: ((player_id: number) => void) | null = null;

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

            this.joinGameCallback!(data.board_size);
        });

        this.socket.on("STONE_PLACED", (payload) => {
            console.log(`STONE_PLACED (${payload})`)
            const data = JSON.parse(payload);

            const game_id = data.game_id;
            const player_id = data.player_id;
            const col = data.col;
            const row = data.row;

            if (game_id !== this.game_id)
                throw new Error("BAD GAME ID");
            this.stonePlacedCallback!(col, row, player_id);
        });

        this.socket.on("STONE_CAPTURED", (payload) => {
            console.log(`STONE_CAPTURED (${payload})`);
            const data = JSON.parse(payload);

            const game_id = data.game_id;
            const captured_stones = data.captured_stones;
            if (game_id !== this.game_id)
                throw new Error("BAD GAME ID");
            this.stoneCapturedCallback!(captured_stones);
        });

        this.socket.on("POINTS", (payload) => {
            console.log(`POINTS (${payload})`);
            const data = JSON.parse(payload);

            const game_id = data.game_id;
            const points = data.points;
            if (game_id !== this.game_id)
                throw new Error("BAD GAME ID");
            this.updatePointsCallback!(points);
        });

        this.socket.on("PLAYER_PASS", (payload) => {
            console.log(`PLAYER_PASS (${payload})`);
            const data = JSON.parse(payload);

            const game_id = data.game_id;
            const player_id = data.player_id;
            if (game_id !== this.game_id)
                throw new Error("BAD GAME ID");
            this.playerPassCallback!(player_id);
        });
    }

    subscribeJoinGameCallback = (callback: (board_size: number) => void) => this.joinGameCallback = callback;
    subscribeStonePlacedCallback = (callback: (col: number, row: number, player_id: number) => void) => this.stonePlacedCallback = callback;
    subscribeStoneCapturedCallback = (callback: (stones: number[][]) => void) => this.stoneCapturedCallback = callback;
    subscribeUpdatePointsCallback = (callback: (points: number[]) => void) => this.updatePointsCallback = callback;
    subscribePlayerPassCallback = (callback: (player_id: number) => void) => this.playerPassCallback = callback;

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

    playerPass = () => {
        const data = {
            "game_id" : this.game_id,
            "player_id" : this.player_id,
        };
        this.socket.emit("player_pass", JSON.stringify(data));
    }
}


export default WebSocketService
