import sqlite3

conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS question(id INTEGER,hint TEXT,link TEXT, PRIMARY KEY(id))')

def add_data(id_,hint,link):
	c.execute('INSERT INTO  question(id,hint,link) VALUES (?,?,?)',(id_,hint,link))
	conn.commit()

def view_data():
	c.execute('SELECT * FROM question')
	data = c.fetchall()
	return data

def get_data(_id):
	c.execute('SELECT * FROM question WHERE id="{}"'.format(_id))
	data = c.fetchall()
	return data

def delete(_id):
	c.execute('DELETE FROM question WHERE id="{}"'.format(_id))
	conn.commit()

def get_id():
	c.execute('Select id from question')
	data = c.fetchall()
	return data 

def update_data(selected_question,id_,hint,link):
	c.execute('UPDATE question SET id=?,hint=?,link=? WHERE id=?',(id_,hint,link,selected_question))
	conn.commit()