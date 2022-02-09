# youtube_highlight_extract
    This is final project in SWjungle

-----

# tech stack
    back-end : flask
    front-end : react 

-----

# back-end

## flask
    flask-restful
    flask-cors

## react
    axios
    make bulid : npm run-script build

## run
    /youtube_highlight_extract/ > pip install flask, flask-restful, flask-cors
    /youtube_highlight_extract/frontend/ npm install axios

    /youtube_highlight_extract/ flask run
    /youtube_highlight_extract/frontend/ npm start
    or
    /youtube_highlight_extract/frontend/ npm run-script build
    /youtube_highlight_extract/ flask run

## pytchat
    ValueError: signal only works in main thread of the main interpreter
    check ref 5.

ref : 
1. https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9
2. https://dev.to/nagatodev/how-to-connect-flask-to-reactjs-1k8i
3. https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project
4. https://docs.python.org/ko/3/library/asyncio-task.html#coroutines
5. https://hashcode.co.kr/questions/13918/thread-%EC%82%AC%EC%9A%A9-%EC%A4%91-valueerror-signal-only-works-in-main-thread-%EC%98%A4%EB%A5%98

-----

# front-end