from flask import Flask,render_template,request,redirect,url_for
import sqlite3
import os

app = Flask(__name__)


conn = sqlite3.connect('gestao_pacientes.db')
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS paciente (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               sexo TEXT,
               cpf TEXT UNIQUE,
               endereco TEXT,
               telefone TEXT
               )
''')

conn.commit()
conn.close()


@app.route('/')
def index():
    database_path = os.path.join(os.path.dirname(__file__), 'gestao_pacientes.db')

    conn = sqlite3.connect(database_path)

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paciente')
    pacientes = cursor.fetchall()
    conn.close()
    return render_template ('index.html' , pacientes=pacientes)

@app.route('/novo_paciente', methods=['GET','POST'])
def novo_paciente():
   if request.method == 'POST':
         nome = request.form['nome']
         idade = request.form['idade']
         sexo = request.form['sexo']
         cpf = request.form['cpf']
         endereco = request.form['endereco']
         telefone = request.form['telefone']   
         print(nome) 
         database_path = os.path.join(os.path.dirname(__file__), 'gestao_pacientes.db')

         conn = sqlite3.connect(database_path)

         conn = sqlite3.connect('gestao_pacientes.db')
         cursor = conn.cursor()
         cursor.execute('''
    INSERT or IGNORE INTO paciente (nome, idade ,sexo, cpf, endereco, telefone)
    VALUES (?,?,?,?,?,?)
''', (nome, idade, sexo, cpf, endereco, telefone))
         conn.commit()
         conn.close()
         return redirect(url_for('index'))
   return render_template('novo_paciente.html')

@app.route('/limpar_pacientes')
def limpar_pacientes():
    database_path = os.path.join(os.path.dirname(__file__), 'gestao_pacientes.db')

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('DELETE  FROM paciente')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)   

