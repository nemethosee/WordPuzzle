class WordPuzzle:
    def __init__(self):
        pass

    def open_puzzle(self, file_name='InputPuzzle.txt'):
        try:
            file = open(file_name, 'r')
        except FileNotFoundError:
            return 'File does not exist!'
        word_list = file.readline()
        file.close()
        return file.name

    def parse_word_list(self, input_string):
        return input_string.split(',')

    def parse_char_list(self, input_string):
        return input_string.split(',')

    def parse_puzzle(self, input_list):
        puzzle = []
        for letter_array in input_list:
            puzzle.append(self.parse_char_list(letter_array))

        return puzzle

    # ToDo: Search horizontally left to right

    # ToDo: Search horizontally right to left

    # ToDo: Search vertically top to bottom

    # ToDo: Search vertically bottom to top

    # ToDo: Search diagonally descending direct order

    # ToDo: Search diagonally descending reverse order

    # ToDo: Search diagonally ascending direct order

    # ToDo: Search diagonally ascending reverse order

    # ToDo: Print out results: [word]: (x1,y1),(x2,y2),...(xn,yn)

    pass