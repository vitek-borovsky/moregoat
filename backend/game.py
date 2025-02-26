class Game:
    def __init__(self, game_id, player_count: int, board_size: int) -> None:
        self.game_id = game_id
        self.player_count = player_count
        self.board_size = board_size
        self.SQUERE_EMPTY = -1
        self.board: list[list[int]] = [ [ self.SQUERE_EMPTY for _ in range(board_size) ] for _ in range(board_size) ]

    def __repr__(self) -> str:
        return f"Game(game_id={ self.game_id }, player_count={ self.player_count }, board_size={ self.board_size })"

    def __getitem__(self, index: tuple[int, int]) -> int:
        col, row = index
        return self.board[row][col]

    def __setitem__(self, index: tuple[int, int], value):
        col, row = index
        self.board[row][col] = value

    def _is_on_board(self, col, row):
        if col not in range(0, self.board_size): return False
        if row not in range(0, self.board_size): return False
        return True

    def _get_neighbours(self, col, row) -> set[tuple[int, int]]:
        neigh = lambda x, y: { (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1) }
        return { (col_, row_) for col_, row_ in neigh(col, row) if self._is_on_board(col_, row_) }

    def print_board(self) -> None:
        print("\n".join([ " ".join([ f"{x:2}" for x in row ]) for row in self.board ]))

    def _get_structure(self, col, row) -> set[tuple[int, int]]:
        """
        Gets all connected stones of given structure

        If col or row are out of range it returns set()
        """
        if not self._is_on_board(col, row): return set()

        structure = set()
        self._get_structure_impl(col, row, self[col, row], structure)
        return structure


    def _get_structure_impl(self, col, row, value, structure) -> None:
        """
        Gets all connected stones of given structure

        If col or row are out of range it returns set()
        """
        if not self._is_on_board(col, row): return
        if self[col, row] != value: return

        if (col, row) in structure: return structure

        structure.add((col, row))
        for col_, row_ in self._get_neighbours(col, row):
            self._get_structure_impl(col_, row_, value, structure)

    def _is_structure_alive(self, structure: set[tuple[int, int]]) -> bool:
        """
        Checks whether a structure is alive acording to go rules:
        - Structure is alive if one of its stones neighbours an empty squere
        """
        for squere in structure:
            for col, row in self._get_neighbours(*squere):
                if self[col, row] == self.SQUERE_EMPTY:
                    return True

        return False

    def _remove_structure(self, structure: set[tuple[int, int]]) -> None:
        """
        Removes stones from the board
        """
        for col, row in structure:
            self[col, row] = self.SQUERE_EMPTY
