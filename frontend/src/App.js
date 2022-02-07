import './App.css';
import React, { useState} from "react";
import axios from 'axios'

function App() {

  const [url, setUrl] = useState('URL : ')
  const inputValue = document.getElementById('link')

  function onChangeUrl(e){
    console.log('call onChangeUrl()')
    if (e.target.value.indexOf('youtube') !== -1)
    {
      console.log('This is Youtube link')
      //  app header class 값을 변경
    }
    setUrl('URL : ' + e.target.value)
  }

  function sendUrl(e)
  {
    console.log('call sendUrl()')
    if (inputValue)
    {
      console.log("인풋창 입력값 : ", inputValue.value)
    }

    axios.get('http://localhost:5000/flask/hello').then(response =>
    {
      console.log("Success", response.data)
    }).catch(error =>
    {
      console.log(error)
    })
  }
  
  return (
    <div className="App">
      <header className="App-header">
        <p>
          유트하(유튜브, 트위치 하이라이트라는 뜻)
        </p>

        <input onChange={onChangeUrl} id='link' />
        <h3>{url}</h3>
        <button onClick={sendUrl}>버튼</button>

      </header>
    </div>
  );
}

export default App;
