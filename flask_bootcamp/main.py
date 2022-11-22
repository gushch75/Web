#from email import message
from flask import Flask, render_template
from auth import LoginForm


app = Flask(__name__)
app.config['SECRET KEY']= 'world world world hello'


@app.route('/',methods= ['GET','POST'])
def main(): 
   """  form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        print (name,surname,email) """
        return render_template('base.html')
      """   ,title='Главная страница',
               form = form,message='Вы авторизовались!')
    return render_template('base.html',title='Главная страница',
               form = form)
  """


   # user_name = ['Aleksey', 'Alla', 'Almir', 'Diana', 'Ilali']
   # return render_template('base.html', user_name=user_name,
                          #   title='Главная страница')


#@app.route('/bootcamp')
#def boot():
 #   return render_template('bootcamp.html', title='BootCamp-tasks')


if __name__ == '__main__':
    app.run()

