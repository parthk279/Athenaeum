// Tutorial used to set up the initial frontend: https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";
import SearchBar from "./components/SearchBar";
import BookData from "./Data.json";
import swal from 'sweetalert';
import Badge from 'react-bootstrap/Badge';

class App extends Component {  // Parent class for all of the Book data
  constructor(props) {
    super(props);
    this.state = {
      viewisInStock: false,     // Variable maintaining availabilty status of books
      bookList: [],
      modal: false,
      activeItem: {
        title: "",
        authors: "",
        isbn: "",
        description: "",
        condition: "",
        price: 0.00,
        link_to_buy: "",
        is_in_stock: false,
      },
    };
  }
  
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/books/")
      .then((res) => this.setState({ bookList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();
    if (item.id) {
      axios
        .put(`/api/books/${item.id}/`, item)
        .then((res) => this.refreshList())
        .catch((err) => console.log(err));
      return;
    }
    axios
      .post("/api/books/", item)
      .then((res) => this.refreshList())
      .catch((err) => console.log(err));
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/books/${item.id}/`)
      .then((res) => this.refreshList())
      .catch((err) => console.log(err));
  };

  createItem = () => {     //Creates a new record
    const item = { title: "", authors: "", isbn: "", description: "", condition: "", price: "", link_to_buy: "", is_in_stock: false };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  displayisInStock = (status) => {    //Function to manipulate availabilty of a book 
    if (status) {
      return this.setState({ viewisInStock: true });
    }

    return this.setState({ viewisInStock: false });
  };

  displayPrice = (item) => {   //Function to display the condition and price of item
    var priceString = '';
    var badgeType = 'info';
    if (item.condition.length > 0) {
      priceString += item.condition + ': ';
      if (item.condition === 'Good') {      //assign a badge type based on the condition 
        badgeType = 'success';
      }
      else if (item.condition === 'Poor') {
        badgeType = 'danger';
      }
      else {
        badgeType = 'warning';
      }
    }
    if (item.price === 0) {
      badgeType = 'secondary';
      priceString += 'Free';
    }
    else {
      priceString += '$' + item.price.toFixed(2).toString();
    }    
    return (
      <Badge pill bg={badgeType}>{priceString}</Badge>
    );
  }

  openExternalLink = (item) => {        //Is called when item does not match any record,
    if (item.link_to_buy.length > 0) {   //redirects to a link to buy the book at original cost
      var win = window.open(item.link_to_buy, '_blank');
      win.focus();
    }
    else {
      swal('There is no link associated with this book yet :(')  
    }
  }

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span
          className={this.state.viewisInStock ? "nav-link active" : "nav-link"}
          onClick={() => this.displayisInStock(true)}
        >
          In Stock
        </span>
        <span
          className={this.state.viewisInStock ? "nav-link" : "nav-link active"}
          onClick={() => this.displayisInStock(false)}
        >
          Out of Stock
        </span>
      </div>
    );
  };

  renderItems = () => {
    const { viewisInStock } = this.state;
    const newItems = this.state.bookList.filter(
      (item) => item.is_in_stock === viewisInStock
    );

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`book-title mr-2 ${
            this.state.viewisInStock ? "isInStock-book" : ""
          }`}
          title={item.description}
        >
          {item.title} - {item.authors}
          <br/>
          {this.displayPrice(item)}{' '}          
        </span>
        <span>
          <button
            className="btn btn-success mr-2"
            onClick={() => this.openExternalLink(item)}
          >
            Buy
          </button>          
          &nbsp; 
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          &nbsp;
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <SearchBar placeholder = "Enter a book name..." data ={BookData}/>
        <h1 className="text-uppercase text-center my-4">Athenaeum</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add book
                </button>
              </div>

              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
      
    );
  }
}

export default App;
