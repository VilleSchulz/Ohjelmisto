let num1 = document.getElementById('num1');
let num2 = document.getElementById('num2');
let operation = document.getElementById('operation');
let result = document.getElementById('result');

document.getElementById('start').addEventListener("click", function (evt) {
        evt.preventDefault();

        let int1 = parseInt(num1.value);
        let int2 = parseInt(num2.value);
        switch (operation.value) {
            case 'add':
                result.innerText = int1 + int2;
                break;
            case 'sub':
                result.innerText = int1 - int2;
                break;
            case 'multi':
                result.innerText = int1 * int2;
                break;
            case 'div':
                if (int2 !== 0) {
                    result.innerText = int1 / int2;
                } else {
                    result.innerText = 'Cannot divide by zero';
                }
                break;
            default :
                result.innerText = 'Invalid operation';
        }


    }
);


