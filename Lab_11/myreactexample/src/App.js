import logo from './logo.svg';
import './App.css';

function HeadingComponent(){
	return (
		<h1>This is my first component</h1>
	)
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <HeadingComponent />
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
