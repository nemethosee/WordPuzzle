import pytest
from WordPuzzle import WordPuzzle


class Test:
    word_puzzle = WordPuzzle()

    def test_puzzle_file_opened_successfully(self):
        expected = 'InputPuzzle.txt'
        actual = self.word_puzzle.open_puzzle()

        assert actual == expected

    def test_puzzle_file_doesnt_exists(self):
        file_name = 'InexistentFile.txt'
        open_result = self.word_puzzle.open_puzzle(file_name)

        assert open_result == 'File does not exist!'

    def test_parse_search_words_input_string(self):
        search_words_string = 'BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA'
        expected_list = ['BONES', 'KHAN', 'KIRK', 'SCOTTY', 'SPOCK', 'SULU', 'UHURA']

        search_word_list = self.word_puzzle.parse_word_list(search_words_string)

        assert search_word_list == expected_list

    def test_parse_letter_array(self):
        input_string = 'U,M,K,H,U,L,K,I,N,V,J,O,C,W,E'
        expected_list = ['U', 'M', 'K', 'H', 'U', 'L', 'K', 'I', 'N', 'V', 'J', 'O', 'C', 'W', 'E']

        letter_list = self.word_puzzle.parse_char_list(input_string)

        assert letter_list == expected_list

    def test_parse_puzzle_content(self):
        input_list = ['U,M,K,H,U,L,K,I,N,V,J,O,C,W,E',
                      'L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G']
        expected_result = [['U', 'M', 'K', 'H', 'U', 'L', 'K', 'I', 'N', 'V', 'J', 'O', 'C', 'W', 'E'],
                           ['L', 'L', 'S', 'H', 'K', 'Z', 'Z', 'W', 'Z', 'C', 'G', 'J', 'U', 'Y', 'G']]

        puzzle = self.word_puzzle.parse_puzzle(input_list)

        assert  puzzle == expected_result

