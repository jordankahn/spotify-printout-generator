async function fetchData(url) {
    console.log(url)
    //Grabs data from Flask server running in backend/flask_app.py
    let response = await fetch('http://192.168.0.7:5000/', {
        method: 'GET',
        headers: new Headers({
            "access-control-allow-origin": "*",
            "spotifyUrl": url
          })
    });
    let songData = await response.json();
    
    return songData
}

export default fetchData