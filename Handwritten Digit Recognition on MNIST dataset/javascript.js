// JavaScript code for drawing, prediction, and clearing
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const predictedDigitElement = document.getElementById('predicted-digit-value');

let isDrawing = false;
let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseout', () => isDrawing = false);

function draw(e) {
    if (!isDrawing) return;
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 5;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.stroke();
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

document.getElementById('submit-btn').addEventListener('click', () => {
    const imageData = canvas.toDataURL();
    predictDigit(imageData);
});

document.getElementById('clear-btn').addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});

function predictDigit(imageData) {
    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify({ image_data: imageData }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(`Predicted digit: ${data.predicted_digit}`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
