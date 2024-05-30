document.addEventListener('DOMContentLoaded', (event) => {
    const openPopupBtn = document.getElementById('openPopupBtn');
    const popup = document.getElementById('popup');
    const closePopupBtn = document.getElementById('closePopupBtn');
    const display = document.getElementById('display');
    let expression = '';

    openPopupBtn.addEventListener('click', () => {
        popup.style.display = 'block';
        popup.style.left = '50px';
        popup.style.top = '50px';
    });

    closePopupBtn.addEventListener('click', () => {
        popup.style.display = 'none';
    });

    function appendNumber(number) {
        expression += number;
        display.value = expression;
    }

    function appendOperator(operator) {
        expression += ` ${operator} `;
        display.value = expression;
    }

    function calculateResult() {
        try {
            const result = eval(expression);
            display.value = result;
            expression = result;
        } catch {
            display.value = 'Error';
            expression = '';
        }
    }

    function clearDisplay() {
        expression = '';
        display.value = '';
    }

    window.appendNumber = appendNumber;
    window.appendOperator = appendOperator;
    window.calculateResult = calculateResult;
    window.clearDisplay = clearDisplay;

    // Dragging functionality
    let isDragging = false;
    let offsetX, offsetY;

    popup.querySelector('.popup-header').addEventListener('mousedown', (e) => {
        isDragging = true;
        offsetX = e.clientX - popup.offsetLeft;
        offsetY = e.clientY - popup.offsetTop;
    });

    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            popup.style.left = `${e.clientX - offsetX}px`;
            popup.style.top = `${e.clientY - offsetY}px`;
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
});
