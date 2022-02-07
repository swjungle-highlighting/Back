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
    //  app header class 값을 변경하면
    }
    setUrl('URL : ' + e.target.value)
  }

  // const sendUrl = (e) => {
  //   console.log('call sendUrl()')
  //
  //   console.log("인풋창 입력값 : ", inputValue.value)
  // }

  function sendUrl(e)
  {
    console.log('call sendUrl()')

    console.log("인풋창 입력값 : ", inputValue.value)
  }


  return (
    <div className="App">
      <header className="App-header">
        {/*<img src={logo} className="App-logo" alt="logo" />*/}
        <p>
          {/*React + Flask Tutorial*/}
          link input
        </p>

          <input onChange={onChangeUrl} id='link' />
          <h3>{url}</h3>
          <button onClick={sendUrl}>버튼</button>

        {/*<div>{getMessage.status === 200 ?*/}
        {/*<h3>{getMessage.data.message}</h3>*/}
        {/*:<h3>LOADING</h3>}*/}
        {/*</div>*/}
      </header>
    </div>
  );
}

export default App;
