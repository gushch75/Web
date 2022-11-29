const age = Number.parseInt(prompt("Введите Ваш возраст :"));
switch (age) 
{
    case 18: 
    alert ('Вы совершеннолетний, все можно!');
    break;
    case 10:
        alert ("Надо учить уроки");
        break;
        case 30:
            alert ("Ложитесь спать, завтра на работу");
            break;
            default:
                alert ("Мы не знаем, что вам делать");
}