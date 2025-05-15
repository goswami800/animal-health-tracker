from flask import Flask, request
import psycopg2

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="animaldb",
        user="postgres",
        password="admin"
    )

@app.route('/add', methods=['POST'])
def add_animal():
    name = request.form['name']
    species = request.form['species']
    health = request.form['health']
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO animals (name, species, health) VALUES (%s, %s, %s);",
                (name, species, health))
    conn.commit()
    cur.close()
    conn.close()
    
    return "Animal added successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')