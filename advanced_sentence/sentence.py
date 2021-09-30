"""Module realize class Sentence"""


class MultipleSentenceError(Exception):
    """
    Class describes MultipleSentenceError
    """
    def __init__(self):
        self.message = "Multiple sentence found"

    def __str__(self):
        return self.message


class Sentence:
    """
    Class realize some additional functionality for  str

    Methods
    -------
    _is_sentence():
        Method checks incoming sentence if sentence not suitable raises error
    _trim_word() -> str:
        Trims all non alphabet symbols from both sides of word and return it
    _is_word(str) -> bool:
        Check str if it word, all symbols is alphabetic returns True, all non alphabetic symbols
        save in list
    _word_counter():
        Counts all 'words' in sentence and save in _words_count attribute.
        Counts only words for those _is_word() returns True
    __getitem(index):
        Method that allow work with indexes

    Attributes
    ----------
    sentence: str
        contains sentence for further processing
    _space_pos: int
        position of firs space
    _other_char_clothed: bool
        flag that indicates other_chars list doesnt append symbols
    other_chars : list
        List of all non alphabet symbols

    """
    def __init__(self, sentence: str):
        self.sentence = sentence
        self._is_sentence()
        self._other_char_clothed = False
        self._words_count = 0
        self.len = len(sentence)
        self.other_chars = []
        self._words_counter()
        self._space_pos = 0
        self._new_space_pos = 0
        self.__words_count = self._words_count

    def __repr__(self):
        return f"<Sentence(words={self._words_count}, other_chars={len(self.other_chars)})>"

    def _is_sentence(self):
        """
        This method checks incoming string. If it is not string  or sentence
        raise exception:
        if sentence ends not with . ! ? or ... raise ValueError
        if sentence consists from many sentences, has more then one occurrences of . ! ? or ... raise
        MultipleSentencesError


        """
        not_words = ["...", "!", "?", "."]

        if not isinstance(self.sentence, str):
            raise TypeError

        flag = False
        for char in not_words:
            if self.sentence.endswith(char):
                flag = True
        if not flag:
            raise ValueError
        # checking for multiple ? ! or its combinations with other symbols
        non_words_count = 0
        for char in not_words:
            if self.sentence.endswith("...") and char == "."\
                    or self.sentence.endswith(".") and char == ".":
                continue
            non_words_count += self.sentence.count(char)
            if non_words_count > 1:
                raise MultipleSentenceError
        # checking for multiple '.' in sentence
        if self.sentence.endswith(".") and not self.sentence.endswith("...") \
                and self.sentence.count(".") + non_words_count > 1:
            raise MultipleSentenceError
        if self.sentence.endswith("...") and self.sentence.count(".") > 3:
            raise MultipleSentenceError

    def _trim_word(self, word: str):
        """
        Method trims firs and last character in word parameter
        and returns word without it

        """
        if len(word) <= 1:
            return word
        if word.startswith(" "):
            word = word[1:]
        if not(word[-1].isalnum()) :
            if not self._other_char_clothed:
                self.other_chars.append(word[-1])
            word = word[:len(word) - 1]
        return word

    def _is_word(self, word: str):
        """
        Method checks that word argument contains only alphabetic characters
        return True or False and adds all non alphabetic symbols in self.other_characters attribute

        """
        flag = True
        word = self._trim_word(word)
        if len(word) < 1:
            return False
        for ch in word:
            if not ch.isalpha() :
                if ch not in self.other_chars and ch != " ":
                    self.other_chars.append(ch)
                flag = False
        return flag

    def _words_counter(self):
        """
        Method counts words in sentence
        """
        space_count = self.sentence.count(" ")
        space_pos = 0
        for i in range(space_count + 1):
            new_space_pos = self.sentence.find(" ", space_pos + 1)
            if new_space_pos > -1:
                word = self.sentence[space_pos+1:new_space_pos]
            else:
                word = self.sentence[space_pos:self.len]
            if word.startswith(" "):
                word = word[1:]
            if self._is_word(word):
                self._words_count += 1
            space_pos = new_space_pos
        self._other_char_clothed = True

    def _words(self) -> str:
        """
        This method returns words from sentence and decrease word_count,
        if word_count equal
        """

        if self._words_count > 0:
            while True:
                self._new_space_pos = self.sentence.find(" ", self._space_pos + 1)
                if self._new_space_pos > -1:
                    word = self.sentence[self._space_pos:self._new_space_pos]
                else:
                    word = self.sentence[self._space_pos:self.len+1]
                self._space_pos = self._new_space_pos
                if self._is_word(word):
                    self._words_count -= 1
                    yield self._trim_word(word)
        else:
            self._words_count = self.__words_count
            self._space_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._words())

    def __len__(self):
        return self.__words_count

    def __getitem__(self, index):

        slice_res = []
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if start > stop:
                raise IndexError("Stop must be bigger than start")
            for i in range(self._words_count):
                a = next(self._words())
                if start <= i < stop:
                    slice_res.append(a)
            self._words_count = self.__words_count
            self._space_pos = 0
            return slice_res
        else:
            for i in range(self._words_count):
                a = next(self._words())
                if i == index:
                    self._words_count = self.__words_count
                    return a

    @property
    def words(self):
        for _ in range(self._words_count):
            print(self.__next__(), end=" ")
        self._words_counter()
        self._space_pos = 0
        print("")
        return


class SentenceIterator:
    """Iterator class for Sentence class container"""

    def __init__(self, sentence: str):
        self.sentence = sentence

    def __iter__(self):
        return Sentence(self.sentence)


a = Sentence("HUIH, 33Z  zzxxx, dfd, AS zzz.")
print(a)

print(a[1:4])
for z in a:
    print(z)
print(a.other_chars)


word_iter = SentenceIterator("AA aa dsd ds.")
for a in word_iter:
    print(a)














