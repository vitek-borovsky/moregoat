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

    def print_board(self) -> None:
        print("\n".join([ " ".join([ f"{x:2}" for x in row ]) for row in self.board ]))

    def get_structure(self, col, row) -> set[tuple[int, int]]:
        """
        Gets all connected stones of given structure

        If col or row are out of range it returns set()
        """
        if col not in range(0, self.board_size): return set()
        if row not in range(0, self.board_size): return set()

        structure = set()
        self.__get_structure_impl(col, row, self[col, row], structure)
        return structure


    def __get_structure_impl(self, col, row, value, structure):
        """
        Gets all connected stones of given structure

        If col or row are out of range it returns set()
        """
        if col not in range(0, self.board_size): return
        if row not in range(0, self.board_size): return
        if self[col, row] != value: return

        if (col, row) in structure: return structure

        structure.add((col, row))
        self.__get_structure_impl(col - 1, row, value, structure)
        self.__get_structure_impl(col + 1, row, value, structure)
        self.__get_structure_impl(col, row - 1, value, structure)
        self.__get_structure_impl(col, row + 1, value, structure)

        return structure

