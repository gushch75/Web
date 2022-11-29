const number1 = Number.parseInt(prompt("Введите температуру в градусах Цельсия"));
function sum(num1)
{
    result = (9/5)*num1 + 32;
    //return result;
}
sum(number1);
alert(`Значение в Фаренгейтах  ${result.toFixed(1)}`);