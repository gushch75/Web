function hello_user(user_name) {
   // alert('Привет,${user_name }');
    alert(`Тебе ${user_name} лет!`);
}
const user_name = prompt("Введите свое имя");
hello_user(user_name);