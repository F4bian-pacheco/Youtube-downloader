
async function put_path(){
    const path = await eel.get_path()();
    document.getElementById('path').innerHTML = path;
}
put_path();

async function change_directory(){
    const path = await eel.change_directory()();
    document.getElementById('path').innerHTML = path;
}

async function download_js(){
    const mensaje = await eel.download()();
    document.getElementById('error').innerHTML = mensaje;
}

eel.expose(get_path);
function get_path(){
    const elemento = document.getElementById("path");
    const data = elemento.innerHTML;
    console.log(data)
    return data;
}


eel.expose(get_url);
function get_url(){
    const elemento = document.getElementById("url");
    const data = elemento.value;
    return data;
}