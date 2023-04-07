import logo from './logo.svg';
import './App.css';
import HeadingComponent from './components/heading';
import ButtonComponent from './components/button';
import CounterComponent from './components/counter';
import CatFacts from './components/catfacts';
import Booklist from './components/booklist';
import Book from './components/book';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <HeadingComponent name="Adam"/>
        <ButtonComponent />
        <CounterComponent />
        <CatFacts />
        <Booklist />
        <Book id={1} />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
