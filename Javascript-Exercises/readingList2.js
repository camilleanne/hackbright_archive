var BookList = function(books){
    this.booksRead = 0;
	this.booksNotRead = 0;
  	this.lastBook;
    this.bookShelf = books || [];
    this.nextBook;
    this.currentBook;

    this.add = function(book) {
    	this.bookShelf.push(book);
    	if (book.read){
    		if (!this.lastBook) {
	    		this.lastBook = book;
    		} else if (this.lastBook.readDate < book.readDate) {
	    		this.lastBook = book;
    		} 
	   		this.booksRead++;
    	} else if (!this.currentBook){
    		this.currentBook = book;
    		this.booksNotRead++;

    	} else {
    		this.booksNotRead++;
    	}
    }

	this.setNextBook = function(){
        for (var i=0; i<this.bookShelf.length; i++) {
            if (!this.bookShelf[i].read) {
				this.nextBook = this.bookShelf[i];
        	}
    	}
	}

    this.finishCurrentBook = function(){
    	this.currentBook.read = true;
    	this.currentBook.readDate = Date(Date.now);
    	this.lastBook = this.currentBook;
    	this.currentBook = this.nextBook;
    	this.setNextBook();
    	this.booksRead++;
    	this.booksNotRead--;

    	// this.lastBook = this.currentBook;
    	// this.lastBook.read = true;
    	// this.lastBook.readDate = Date(Date.now);
    	// this.currentBook = this.nextBook;
    	// this.setNextBook();
    	// this.booksRead++;
    	// this.booksNotRead--;
    }
}

var Book = function(title, author, genre, imgURL, read, readdate){
	this.title = title || "No Title"; 
	this.author = author || "No Author";
	this.genre = genre || "Fiction";
	this.read = read || false;
	this.readDate = new Date(readdate);
	this.imgURL = imgURL || null;
}

lordOfTheRings = new Book("Lord of the Rings", "J.R.R. Tolkien", "Fantasy");
gameOfThrones = new Book("Game of Thrones", "George Martin", "Fantasy");
wutheringHeights = new Book("Wuthering Heights", "Bronte", "Romance");
aliceInWonderland = new Book("Alice in Wonderland", "Lewis Carroll", "Romance", true, "2011, 10, 1");

var myBooks = new BookList()

var someBooks = [lordOfTheRings,gameOfThrones, wutheringHeights, aliceInWonderland]

//looping through this is more efficient/less shitty
for (var i = someBooks.length - 1; i >= 0; i--) {
	myBooks.add(someBooks[i])
};