
async function put_path() {
    const path = await eel.get_path()();
    document.getElementById('path').innerHTML = path;
}
put_path();

async function change_directory() {
    const path = await eel.change_directory()();
    document.getElementById('path').innerHTML = path;
}

async function download_js() {
    const mensaje = await eel.download()();
    document.getElementById('error').innerHTML = mensaje;
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
    const ext = document.getElementsByName("ext");
    const mp3 = ext[0];
    const mp4 = ext[1];
    var data_ext;

    if (mp3.checked && mp4.checked) {
        console.log("error");
    } else if (mp3.checked) {
        data_ext = mp3.id;
    } else if (mp4.checked) {
        data_ext = mp4.id;
    }
    const data = { "url": elemento.value, "ext": data_ext };
    return data;
}