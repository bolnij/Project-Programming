import os
import sqlite3
import logging
import re
from datetime import datetime, date
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_sekreta_atslega_2026'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lietotaji (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lietotajvards TEXT UNIQUE NOT NULL,
                    parole TEXT NOT NULL,
                    loma TEXT DEFAULT 'user')''')    
    c.execute('''CREATE TABLE IF NOT EXISTS majasdarbi (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prieksmets TEXT NOT NULL,
                    uzdevums TEXT NOT NULL,
                    terminis TEXT,
                    statuss TEXT DEFAULT 'Nav pabeigts',
                    lietotaja_id INTEGER,
                    FOREIGN KEY(lietotaja_id) REFERENCES lietotaji(id))''')    
    try:
        admins_eksiste = c.execute('SELECT * FROM lietotaji WHERE lietotajvards = ?', ('admin',)).fetchone()
        if not admins_eksiste:
            hashed_pw = generate_password_hash('admin123')
            c.execute("INSERT INTO lietotaji (lietotajvards, parole, loma) VALUES (?, ?, ?)", 
                      ('admin', hashed_pw, 'admin'))
    except sqlite3.Error as e:
        logging.error(f"DB Error: {e}")
    conn.commit()
    conn.close()

init_db()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        
        if len(username) < 4:
            flash('Lietotājvārdam jābūt vismaz 4 simbolus garam!')
            return redirect(url_for('register'))
        if not re.match("^[a-zA-Z0-9_]*$", username):
            flash('Lietotājvārds drīkst saturēt tikai burtus un ciparus!')
            return redirect(url_for('register'))
        if len(password) < 6:
            flash('Parolei jābūt vismaz 6 simbolus garai!')
            return redirect(url_for('register'))
            
        conn = get_db_connection()
        try:
            hashed_pw = generate_password_hash(password)
            conn.execute('INSERT INTO lietotaji (lietotajvards, parole) VALUES (?, ?)', (username, hashed_pw))
            conn.commit()
            flash('Reģistrācija veiksmīga! Tagad variet pieteikties.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Šāds lietotājvārds jau ir aizņemts!')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        lietotajvards = request.form['username']
        parole = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM lietotaji WHERE lietotajvards = ?', (lietotajvards,)).fetchone()
        conn.close()
        if user and check_password_hash(user['parole'], parole):
            session['user_id'] = user['id']
            session['username'] = user['lietotajvards']
            session['loma'] = user['loma']
            return redirect(url_for('index'))
        flash('Nepareizs lietotājvārds vai parole!')
    return render_template('login.html')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    search = request.args.get('search', '').strip()
    status_filter = request.args.get('filter', 'Visi')
    conn = get_db_connection()
    
    query = 'SELECT * FROM majasdarbi WHERE lietotaja_id = ?'
    params = [session['user_id']]
    
    if status_filter != 'Visi':
        query += ' AND statuss = ?'
        params.append(status_filter)
    if search:
        query += ' AND (prieksmets LIKE ? OR uzdevums LIKE ?)'
        params.extend([f'%{search}%', f'%{search}%'])
    
    query += ' ORDER BY prieksmets DESC, terminis ASC'
    
    tasks = conn.execute(query, params).fetchall()
    conn.close()
    
    today = date.today().isoformat()
    
    return render_template('index.html', tasks=tasks, current_filter=status_filter, today=today)

@app.route('/create', methods=['POST'])
def create():
    if 'user_id' not in session: return redirect(url_for('login'))
    
    prieksmets = request.form['subject'].strip().capitalize()
    uzdevums = request.form['task'].strip()
    date = request.form['date']
    
    if len(prieksmets) < 2 or len(uzdevums) < 3:
        flash('Ievadītie dati ir pārāk īsi!')
        return redirect(url_for('index'))
        
    conn = get_db_connection()
    conn.execute('INSERT INTO majasdarbi (prieksmets, uzdevums, terminis, lietotaja_id) VALUES (?, ?, ?, ?)', 
                 (prieksmets, uzdevums, date, session['user_id']))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    hw = conn.execute('SELECT * FROM majasdarbi WHERE id = ? AND lietotaja_id = ?', (id, session['user_id'])).fetchone()
    
    if request.method == 'POST':
        conn.execute('UPDATE majasdarbi SET prieksmets=?, uzdevums=?, terminis=? WHERE id=?', 
                     (request.form['subject'].strip().capitalize(), request.form['task'].strip(), request.form['date'], id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('edit.html', hw=hw)

@app.route('/complete/<int:id>')
def complete(id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute("UPDATE majasdarbi SET statuss = 'Izpildīts' WHERE id = ? AND lietotaja_id = ?", (id, session['user_id']))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/priority/<int:id>')
def change_priority(id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM majasdarbi WHERE id = ? AND lietotaja_id = ?', (id, session['user_id'])).fetchone()
    if task:
        cur = task['prieksmets']
        new_v = cur.replace('⭐ ', '', 1) if cur.startswith('⭐ ') else '⭐ ' + cur
        conn.execute("UPDATE majasdarbi SET prieksmets = ? WHERE id = ?", (new_v, id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute('DELETE FROM majasdarbi WHERE id = ? AND lietotaja_id = ?', (id, session['user_id']))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if session.get('loma') != 'admin':
        flash('Piekļuve liegta!')
        return redirect(url_for('index'))
    conn = get_db_connection()
    stats = {
        'users': conn.execute('SELECT COUNT(*) FROM lietotaji').fetchone()[0],
        'tasks': conn.execute('SELECT COUNT(*) FROM majasdarbi').fetchone()[0]
    }
    all_users = conn.execute('SELECT id, lietotajvards, loma FROM lietotaji').fetchall()
    conn.close()
    return render_template('admin.html', stats=stats, users=all_users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)" " 
