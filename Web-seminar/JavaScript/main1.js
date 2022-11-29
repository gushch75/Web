function sum(num1, num2) {
    const result = num1 + num2;
    return result;
}
const number1 = Number.parseInt(prompt("Введите первое число"));
const number2 = Number.parseInt(prompt("Введите второе число"));

//const result = number1+ number2;
const result = sum(number1, number2);
alert(result);