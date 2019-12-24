import sys
import re

class Indices:

    def __init__(self, datafile="bibletaxonomy.csv"):
        self.indices = {}
        self.book_names = []
        self.total_books = 0
        self.total_chapters = 0
        self.total_verses = 0


        with open(datafile, "r") as f:
            for line in f:
                book, chapter, verse = line.strip().split(",")
                chapter = int(chapter)
                verse = int(verse)
                self._add_entry(book, chapter, verse)

        print('Loaded indices ({} books, {} chapters, {} verses)'.format(self.total_books, self.total_chapters, self.total_verses))

    
    def _add_entry(self, book, chapter, verse):
        # print(book, chapter, verse)
        # sys.exit(0)
        if book not in self.indices:
            self.indices[book] = {}
            self.total_books += 1
            self.book_names.append(book)

        if chapter not in self.indices[book]:
            self.indices[book][chapter] = [verse]
            self.total_chapters += 1
        else:
            self.indices[book][chapter].append(verse)
        self.total_verses += 1

    def get_books(self):
        return list(self.indices.keys())
    def get_chapters(self, book):
        return list(self.indices[book].keys())
    def get_verses(self, book, chapter):
        return self.indices[book][chapter]
    def get_book_name_index(self, book_name):
        return self.book_names.index(book_name)
    

if __name__ == '__main__':
    indices = Indices()
    # print(indices.indices)
    # print(indices.get_chapters('Genesis'))
    print(indices.get_verses('Genesis', 1))

        



