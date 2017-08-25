BookList = function() {
    this.booksRead = 0;
    this.booksNotRead = 0;
    this.bookShelf = [];
    this.currentBook;
    this.lastBook;
    this.nextBook;

    this.nextBook = function(){
         for (var i=0; i<this.bookShelf.length; i++) {
            if (this.bookShelf[i].read === false) {
                return this.bookShelf[i];
            }
        }
        console.log("Finished reading all books");
        return null;
    }
    this.setCurrentBook = function(Book){
        this.currentBook = Book;
    }
    this.getCurrentBook = function() {
        return this.currentBook;
    }
    this.add = function(Book) {
        this.bookShelf.push(Book);
        this.booksNotRead++;
    }
    this.finishCurrentBook = function(Book) {
        Book.read = true;
        Book.readDate = new Date(Date.now());
        this.booksRead++;
        this.booksNotRead--; 
        this.lastBook = Book;
        nextBook = this.nextBook();
        this.setCurrentBook(nextBook);
     }
}

Book = function(Title, Genre, Author) {
    this.Title = Title;
    this.Genre = Genre;
    this.Author = Author;
    this.read = false;
    this.readDate;
}

bookList = new BookList();
book1 = new Book("Harry Potter", "Fantasy", "J.K. Rowling");
book2 = new Book("Lord of the Rings", "Fantasy", "J.R.R. Tolkien");
book3 = new Book("Romeo and Juliet", "Love Story", "Shakespeare");
bookList.add(book1);
bookList.add(book2);
bookList.add(book3);
bookList.setCurrentBook(book1);
bookList.finishCurrentBook(book1);
bookList.finishCurrentBook(bookList.getCurrentBook());