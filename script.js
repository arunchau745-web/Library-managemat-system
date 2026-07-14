let books=[];

function addBook(){

    let id=document.getElementById("bookId").value;
    let title=document.getElementById("title").value;
    let author=document.getElementById("author").value;

    if(id=="" || title=="" || author==""){
        alert("Fill all fields");
        return;
    }

    books.push({
        id:id,
        title:title,
        author:author,
        issued:false
    });

    displayBooks();

    document.getElementById("bookId").value="";
    document.getElementById("title").value="";
    document.getElementById("author").value="";
}

function displayBooks(){

    let table=document.getElementById("bookTable");

    table.innerHTML="";

    books.forEach((book,index)=>{

        table.innerHTML+=`
        <tr>
        <td>${book.id}</td>
        <td>${book.title}</td>
        <td>${book.author}</td>
        <td>${book.issued?"Issued":"Available"}</td>

        <td>

        <button class="issue"
        onclick="issueBook(${index})">
        Issue
        </button>

        <button class="return"
        onclick="returnBook(${index})">
        Return
        </button>

        </td>

        </tr>
        `;

    });

}

function issueBook(index){
    books[index].issued=true;
    displayBooks();
}

function returnBook(index){
    books[index].issued=false;
    displayBooks();
}