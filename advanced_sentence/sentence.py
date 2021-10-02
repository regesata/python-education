"""Module realize class Sentence"""


class MultipleSentenceError(Exception):
    """
    Class describes MultipleSentenceError
    """
    def __init__(self):
        self.message = "Multiple sentence found"
        super().__init__()

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

        position of firs space


    """
    def __init__(self, sentence: str):
        self.sentence = sentence
        self._is_sentence()
        self.curr_pos = 0
        self.curr_word = ""
        self._words_count = 0
        self._other_words_count = 0
        self.len = len(sentence)
        self._words_counter()

    def __repr__(self):
        return f"<Sentence(words={self._words_count}, other_chars={self._other_words_count})>"

    def _is_sentence(self):
        """
        This method checks incoming string.
        If it is not string  or sentence
        raise exception:
        if sentence ends not with . ! ? or ... raise ValueError
        if sentence consists from many sentences, has more then
        one occurrences of . ! ? or ... raise
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

    def _words_counter(self):
        """
        Method counts words in sentence
        """
        curr_word = ""
        cur_pos = 0
        words_count = 0
        other_words_count = 0
        while cur_pos < len(self.sentence):
            if self.sentence[cur_pos].isalnum():
                curr_word += self.sentence[cur_pos]
                cur_pos += 1
            elif len(curr_word) > 0:
                curr_word = ""
                words_count += 1
            else:
                cur_pos += 1
                other_words_count += 1
                curr_word = ""
        self._other_words_count = other_words_count
        self._words_count = words_count

    def _words(self) -> str:
        """
        This method returns words from sentence.

        """
        curr_word = ""
        while self.curr_pos < self.len:
            if self.sentence[self.curr_pos].isalnum():
                curr_word += self.sentence[self.curr_pos]
                self.curr_pos += 1
            elif len(curr_word) > 0:
                self.curr_pos += 1
                yield curr_word
            else:
                self.curr_pos += 1
        self.curr_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._words())

    def __len__(self):
        return self._words_count

    def __getitem__(self, index):
        slice_res = ""
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if start > stop:
                raise IndexError("Stop must be bigger than start")
            for ind in range(self._words_count):
                word = next(self._words())
                if start <= ind < stop:
                    slice_res += word + " "
            self.curr_pos = 0
            return slice_res

        for ind in range(self._words_count):
            slice_res = next(self._words())
            if ind == index:
                self.curr_pos = 0
                return slice_res

    @property
    def words(self):
        """
        Property that returns all word in sentence
        :return: str
        """
        curr_word = ""
        res = []
        curr_pos = 0

        while curr_pos < self.len:
            if self.sentence[curr_pos].isalnum():
                curr_word += self.sentence[curr_pos]
                curr_pos += 1
            elif len(curr_word) > 0:
                curr_pos += 1
                res.append(curr_word)
                curr_word = ""
            else:
                curr_pos += 1

        return " ".join(res)

    @property
    def other_chars(self):
        """
        Property that returns all non words in sentence
        :return: str
        """

        curr_word = ""
        curr_pos = 0

        while curr_pos < self.len:
            if not self.sentence[curr_pos].isalnum():
                curr_word += "'" + self.sentence[curr_pos] + "'"
                curr_pos += 1
            elif len(curr_word) > 0:
                curr_pos += 1
            else:
                curr_pos += 1

        return curr_word

class SentenceIterator:
    """Iterator class for Sentence class container"""

    def __init__(self, sentence: str):
        self.sen = Sentence(sentence)

    def __iter__(self):
        return self.sen

    def __next__(self):
        return next(self.sen)


a = Sentence("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
print(a._words())
print(a[1:4])
print(a.words)
print(a.other_chars)
print(next(a))
print(next(a))

word_iter = SentenceIterator("Lorem Ipsum is simply dummy text.")
for item in iter(word_iter):
    print(item)

print(next(word_iter))
print(next(word_iter))
