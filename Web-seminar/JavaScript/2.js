function hello_user(user_name) {
    // alert('Привет,${user_name }');
     alert(`Приветствую тебя на нашей странице, ${user_name}`);
 }
 const user_name = prompt("Введите свое имя");
 hello_user(user_name);