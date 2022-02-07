import './App.css';
import React, {useEffect, useState} from "react";
import axios from 'axios'

function App() {

  const [url, setUrl] = useState('URL : ')
  const inputValue = document.getElementById('link')

  function onChangeUrl(e){
    console.log('call onChangeUrl()')
    if (e.target.value.indexOf('youtube') != -1)
    {
      console.log('This is Youtube link')
      //  app header class 값을 변경
    }
    setUrl('URL : ' + e.target.value)
  }

  function sendUrl(e)
  {
    console.log('call sendUrl()')
    console.log("인풋창 입력값 : ", inputValue.value)
  }
  
  return (
    <div className="App">
      <header className="App-header">
        <p>
          link input
        </p>

        <input onChange={onChangeUrl} id='link' />
        <h3>{url}</h3>
        <button onClick={sendUrl}>버튼</button>

      </header>
    </div>
  );
}

export default App;
