const canvas = document.getElementById('drawCanvas');
const ctx = canvas.getContext('2d');

ctx.fillStyle = 'white';
ctx.fillRect(0, 0, canvas.width, canvas.height);

let drawing = false;

canvas.addEventListener('mousedown', (e) => {
    drawing = true;
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
});

canvas.addEventListener('mousemove', (e) => {
    if (drawing) {
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    }
});

canvas.addEventListener('mouseup', () => {
    drawing = false;
});

canvas.addEventListener('mouseleave', () => {
    drawing = false;
});

canvas.addEventListener('touchstart', (e) => {
    e.preventDefault();
    const touch = e.touches[0];
    const pos = getTouchPos(touch);
    drawing = true;
    ctx.beginPath();
    ctx.moveTo(pos.x, pos.y);
});

canvas.addEventListener('touchmove', (e) => {
    e.preventDefault();
    if (drawing) {
    const touch = e.touches[0];
    const pos = getTouchPos(touch);
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();
    }
});

canvas.addEventListener('touchend', (e) => {
    e.preventDefault();
    drawing = false;
});

function getTouchPos(touch) {
    const rect = canvas.getBoundingClientRect();
    return {
    x: touch.clientX - rect.left,
    y: touch.clientY - rect.top
    };
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function sendCanvas() {
    const base64Data = canvas.toDataURL("image/png").replace(/^data:image\/png;base64,/, '');
    document.getElementById('msgInput').value = base64Data;
    document.getElementById('prmpInput').value = 'This is an image drawn by a human on a blank canvas. Do not describe the canvas, background, tools, or drawing style. Focus only on what is represented in the image — the subject and the objects that the person tried to depict.  Output exactly 10 emojis that best represent the *content* of the drawing. Do not explain. No words. No symbols. No punctuation. No artistic or abstract emoji.  Only output a single line with 10 emojis that match what was drawn.'
    sendMessage();
}