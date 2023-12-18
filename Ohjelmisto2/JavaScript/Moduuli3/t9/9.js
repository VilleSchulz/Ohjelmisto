let operation = document.getElementById('calculation');
let result = document.getElementById('result');
let calculation;
document.getElementById('start').addEventListener("click", function (evt) {
        evt.preventDefault()
    let operationValue = operation.value;
        switch (true) {
            case operationValue.includes("+"):
                calculation = operationValue.split('+');
                result.innerText = parseInt(calculation[0]) + parseInt(calculation[1]);
                break;
            case operationValue.includes("-"):
                calculation = operationValue.split('-');
                result.innerText = parseInt(calculation[0]) - parseInt(calculation[1]);
                break;
           case operationValue.includes("*"):
                calculation = operationValue.split('*');
                result.innerText = parseInt(calculation[0]) * parseInt(calculation[1]);
                break;
            case operationValue.includes("/"):
                calculation = operationValue.split('/');
                if (calculation[1] !== 0) {
                    result.innerText = parseInt(calculation[0]) / parseInt(calculation[1]);
                } else {
                    result.innerText = "Cannot divide by zero";
                }
                break;
            default:
                result.innerText = "Invalid operation";
        }
    }
)
