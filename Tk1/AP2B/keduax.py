from flask import Flask, request, redirect

app = Flask(__name__)

# membuat dictionary user
users = {
    "Faris": "farisaja"
}


# membuat halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # jika metode permintaan adalah POST
    if request.method == 'POST':
        # cek apakah username dan password ada dalam dictionary user
        if request.form['username'] in users and request.form['password'] == users[request.form['username']]:
            # redirect ke halaman utama jika login berhasil
            return redirect('/main')
        else:
            # tampilkan pesan error jika login gagal
            return "Invalid username or password"
    # tampilkan halaman login jika metode permintaan adalah GET
    return '''
        <style>
            
            label {
                display: block;
                margin-bottom: 10px;
                
            }
            input[type=submit] {
            display: block;
            margin-top: 10px;
            }
        </style>
        <form method="post">
            <label>Username:</label>
            <input type="text" name="username">
            <label>Password:</label>
            <input type="password" name="password">
            <input type="submit" value="Submit">
        </form>
    
    '''

# membuat halaman utama setelah login berhasil
@app.route('/main')
def main():
    return '''
        <h1>Selamat datang Faris</h1>
        '''

if __name__ == '__main__':
    app.run()