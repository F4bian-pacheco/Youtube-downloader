
async function put_path() {
    const path = await eel.get_path()();
    document.getElementById('path').innerHTML = path;
}
put_path();

async function change_directory() {
    const path = await eel.change_directory()();
    document.getElementById('path').innerHTML = path;
}

async function get_info_js() {
    var info = await eel.get_info()();
    var info_js = JSON.parse(info)


    var streams = info_js.stream_list
    var streams = streams.slice(1, -1)
    var streams = streams.split(",")

    var sizes = info_js.stream_size
    var sizes = sizes.slice(1, -1)
    var sizes = sizes.split(",")

    for (let i = 0; i < streams.length; i++) {
        const element = streams[i];
        document.getElementById('info').innerHTML += `
            <div class="info-content">
                <img src='${info_js.img}'>
                <span>
                    <h5>${element}</h5>
                    <h6> ${info_js.titulo} <br> ${sizes[i]}Mb </h6>

                </span>
                <input type="checkbox" name='${element}' class='descargar' id='${i}'>
            </div>
        `;
    }
}

//eel.expose(send_data)
function send_data() {
    const el = document.querySelectorAll(".descargar")
    let arr_checkeds = []
    el.forEach(li => {
        if (li.checked) {
            arr_checkeds.push(li.name)
        }
    })
    console.log(arr_checkeds)
    return arr_checkeds

}

async function download_js() {
    data = send_data()
    url = get_data()["url"]
    console.log(url)
    path = document.getElementById('path').innerHTML
    document.getElementById('error').innerHTML = "descargando";

    myLoop();
    await eel.download(data, url, path)();
    document.getElementById('error').innerHTML = " ";
}


eel.expose(get_path);
function get_path() {
    const elemento = document.getElementById("path");
    const data = elemento.innerHTML;
    console.log(data)
    return data;
}


eel.expose(get_data);
function get_data() {
    const elemento = document.getElementById("url");
    const data = { "url": elemento.value };
    return data;
}


const progress = document.getElementById("prog");

console.log(progress.value);

var i = 1;                  //  set your counter to 1

function myLoop() {         //  create a loop function
    setTimeout(function () {   //  call a 3s setTimeout when the loop is called
        progress.value = i;
        i++;                    //  increment the counter
        if (i < 101) {           //  if the counter < 10, call the loop function
            myLoop();             //  ..  again which will trigger another 
        }                       //  ..  setTimeout()
    }, 200)
}