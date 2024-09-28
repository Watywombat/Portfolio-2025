const showTextBtn = document.getElementById('showTextBtn');
const textZone = document.getElementById('textZone');
const closeBtn = document.getElementById('closeBtn');

showTextBtn.addEventListener('click', () => {
    textZone.style.display = 'flex';
    closeBtn.style.display = 'block';
    showTextBtn.style.display = 'none';
});

closeBtn.addEventListener('click', () => {
    textZone.style.display = 'none';
    closeBtn.style.display = 'none';
    showTextBtn.style.display = 'block';
});