from .error import SelfCapture, SquareOccuptied, NotOnBoard


class Board:
    def __init__(self, player_count: int, board_size: int) -> None:
        self.player_count = player_count
        self.board_size = board_size
        self.SQUERE_EMPTY = -1
        self.board: list[list[int]] = [
            [self.SQUERE_EMPTY for _ in range(board_size)]
            for _ in range(board_size)]

    def __repr__(self) -> str:
        return f"""Board(
            player_count={ self.player_count },
            board_size={ self.board_size })"""

    def __getitem__(self, index: tuple[int, int]) -> int:
        col, row = index
        return self.board[row][col]

    def __setitem__(self, index: tuple[int, int], value):
        col, row = index
        self.board[row][col] = value

    def _is_on_board(self, col, row):
        if col not in range(0, self.board_size):
            return False
        if row not in range(0, self.board_size):
            return False
        return True

    def _get_neighbours(self, col, row) -> set[tuple[int, int]]:
        def neigh(x: int, y: int):
            return {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}

        return {(col_, row_)
                for col_, row_ in neigh(col, row)
                if self._is_on_board(col_, row_)}

    def print_board(self) -> None:
        print("\n".join(
            [" ".join([f"{x:2}" for x in row])
                for row in self.board]))

    def _get_structure(self, col, row) -> set[tuple[int, int]]:
        """
        Gets all connected stones of given structure

        If col or row are out of range it returns set()
        """
        if not self._is_on_board(col, row):
            return set()

        structure = set()
        self._get_structure_impl(col, row, self[col, row], structure)
        return structure

    def _get_structure_impl(self, col, row, value, structure) -> None:
        """
        Gets all connected stones of given structure

        If col or row are out of range it returns set()
        """
        if not self._is_on_board(col, row):
            return

        if self[col, row] != value:
            return

        if (col, row) in structure:
            return structure

        structure.add((col, row))
        for col_, row_ in self._get_neighbours(col, row):
            self._get_structure_impl(col_, row_, value, structure)

    def _is_structure_alive(self, structure: set[tuple[int, int]]) -> bool:
        """
        Checks whether a structure is alive acording to go rules:
        - Structure is alive if one of its stones neighbours an empty square
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

    def place_stone(
            self, col: int, row: int, player_id: int
            ) -> tuple[list[int], set[tuple[int, int]]]:
        """
        Places a stone of given player and removes captured stones

        Args:
            col: column where to place stone
            row: row where to place stone
            player_id: player_id of player that is placing stones

        Errors:
            - NotOnBoard - invalid (col,row) pair is supplied
            - SquareOccuptied - Square not empty

        Returns:
            - The list of stones captured per player
              rv[i] == player captured rv[i] stones of player with id i
            - The list of all captured stones
        """
        # TODO cleanup this horrible function
        if not self._is_on_board(col, row):
            raise NotOnBoard(f"({col}, {row}) is not a valid square")

        if self[col, row] != self.SQUERE_EMPTY:
            raise SquareOccuptied(
                f"""On ({col}, {row}) is occupied.
                Already occupied by player {self[col, row]}""")

        self[col, row] = player_id
        neighbours = self._get_neighbours(col, row)
        neighbour_structures = []
        for neigh in neighbours:
            st = self._get_structure(*neigh)
            if st in neighbour_structures:
                continue
            neighbour_structures.append(st)

        # remove self-structure
        if self._get_structure(col, row) in neighbour_structures:
            neighbour_structures.remove(self._get_structure(col, row))

        point_changes_per_player = [0 for _ in range(self.player_count)]

        # We need to mark dead structures first because they can be
        # from diffrent players
        # and capturing one can make the other "alive"
        marked_structures: list[set[tuple[int, int]]] = []
        for st in neighbour_structures:
            if not self._is_structure_alive(st):
                marked_structures.append(st)

        for st in marked_structures:
            col, row = list(st)[0]
            captured_player_id = self[col, row]
            point_changes_per_player[captured_player_id] += len(st)
            self._remove_structure(st)

        self_structure = self._get_structure(col, row)
        if marked_structures == [] \
                and not self._is_structure_alive(self_structure):
            self[col, row] = self.SQUERE_EMPTY
            raise SelfCapture(f"""Cannot place stone on ({col}, {row})
              would resolve in a self capture (placing in an eye)""")

        marked_points = set()
        for st in marked_structures:
            marked_points |= st

        return point_changes_per_player, marked_points
