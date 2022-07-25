// ---- Estructura de datos ----
let data = {
    luz: 0,
    volar: 0,
    motores: [0, 0, 0, 0],
    joystick: {x: 0, y: 0}, 
}

let socket_connected = false;

// ---- Elementos del HTML ----
const slight = document.querySelector("#slight");

const m1 = document.querySelector("#sM1");
const m2 = document.querySelector("#sM2");
const m3 = document.querySelector("#sM3");
const m4 = document.querySelector("#sM4");

m1.disabled = true;
m2.disabled = true;
m3.disabled = true;
m4.disabled = true;

// --- Funciones de ayuda ----
function updateEngineState(state) {
    if(state == true) {
        data.volar = 1;
        data.motores[0] = 1;
        m1.checked = true;
        m1.disabled = false;
        data.motores[1] = 1;
        m2.checked = true;
        m2.disabled = false;
        data.motores[2] = 1;
        m3.checked = true;
        m3.disabled = false;
        data.motores[3] = 1;
        m4.checked = true;
        m4.disabled = false;
    } else {
        data.volar = 0;
        data.motores[0] = 0;
        m1.checked = false;
        m1.disabled = true;
        data.motores[1] = 0;
        m2.checked = false;
        m2.disabled = true;
        data.motores[2] = 0;
        m3.checked = false;
        m3.disabled = true;
        data.motores[3] = 0;
        m4.checked = false;
        m4.disabled = true;
    }
}

function sendActuadorUpdate(actuador) {
    if (socket_connected == true){
        if(actuador == "volar") {
            socket.emit("volar_event", data.volar);
        }
        if(actuador == "luz") {
            socket.emit("luz_event", data.luz);
        }
        if(actuador == "motores") {
            socket.emit("motores_event", data.motores);
        }
        if(actuador == "joystick") {
            socket.emit("joystick_event", data.joystick);
        }
    }
}

// ---- Instanciar elementos HTML y conectar eventos ----

joystick.ondrag = function(){
    data.joystick.x = this.shaft.current.abs_vector.x;
    data.joystick.y = this.shaft.current.abs_vector.y;
    sendActuadorUpdate("joystick");
}

m1.onchange = (e) => {
    data.motores[0] = e.target.checked;
    sendActuadorUpdate("motores");
}
m2.onchange = (e) => {
    data.motores[1] = e.target.checked;
    sendActuadorUpdate("motores");
}
m3.onchange = (e) => {
    data.motores[2] = e.target.checked;
    sendActuadorUpdate("motores");
}
m4.onchange = (e) => {
    data.motores[3] = e.target.checked;
    sendActuadorUpdate("motores");
}

slight.onchange = (e) => {
    const val = e.target.checked ? 1 : 0;
    data.luz = val;
    sendActuadorUpdate("luz");
}
const sengine = document.querySelector("#sengine");
sengine.onchange = (e) => {
    updateEngineState(e.target.checked);
    sendActuadorUpdate("volar");
    sendActuadorUpdate("motores");
}

// ---- Web sockets contra el backend ----
let socket = io();
socket.on("connect", function() {
    socket_connected = true;
    socket.on('luz_1', function (msg) {
        const val = Number(msg);
        data.luz = val;
        slight.checked = val;
    });
    socket.on('volar', function (msg) {
        const val = Number(msg);
        sengine.checked = val;
        updateEngineState(val);
    });
    socket.on('motor_1', function (msg) {
        // Si el está activado el vuelo
        // permito actualizar el estado del motor
        if(data.volar == true) {
            const val = Number(msg);
            data.motores[0] = msg;
            m1.checked = msg;
        }
    });
    socket.on('motor_2', function (msg) {
        // Si el está activado el vuelo
        // permito actualizar el estado del motor
        if(data.volar == true) {
            const val = Number(msg);
            data.motores[1] = msg;
            m2.checked = msg;
        }
    });
    socket.on('motor_3', function (msg) {
        // Si el está activado el vuelo
        // permito actualizar el estado del motor
        if(data.volar == true) {
            const val = Number(msg);
            data.motores[2] = msg;
            m3.checked = msg;
        }
    });
    socket.on('motor_4', function (msg) {
        // Si el está activado el vuelo
        // permito actualizar el estado del motor
        if(data.volar == true) {
            const val = Number(msg);
            data.motores[3] = msg;
            m4.checked = msg;
        }
    });
});
