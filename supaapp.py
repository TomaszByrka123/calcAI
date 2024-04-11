from flask import Flask, request, jsonify, redirect, url_for, session
from supabase import create_client

# Tworzenie instancji aplikacji Flask
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Konfiguracja danych dostępowych do Supabase
SUPABASE_URL = 'https://qgvdmudlnfpspdbzopxh.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFndmRtdWRsbmZwc3BkYnpvcHhoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMTM5NzY3NSwiZXhwIjoyMDI2OTczNjc1fQ.DrLdEt_hHptoC2iYCSRacIqd_ELFLeoCC34XhOLiG9k'

# Inicjalizacja klienta Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Strona główna aplikacji
@app.route('/')
def index():
    if 'user' in session:
        return 'Witaj, ' + session['user'] + '! <a href="/logout">Wyloguj się</a>.'
    else:
        return 'Witaj! Zaloguj się <a href="/login">tutaj</a>.'

# Strona logowania
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Logowanie za pomocą adresu e-mail i hasła
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})

        print(response)

        if response['status_code'] == 200:
            session['user'] = email  # Zapisanie adresu e-mail w sesji
            return redirect(url_for('index'))
        else:
            return 'Nieprawidłowe dane logowania. Spróbuj ponownie.'

    return '''
        <form method="post">
            <p>E-mail: <input type="text" name="email"></p>
            <p>Hasło: <input type="password" name="password"></p>
            <p><input type="submit" value="Zaloguj"></p>
        </form>
    '''

# Strona wylogowania
@app.route('/logout')
def logout():
    session.pop('user', None)  # Usunięcie użytkownika z sesji
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)