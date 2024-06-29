from flask import Flask, render_template, request, redirect
import os

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}

@app.route("/", methods= ["GET", "POST"])
def home():
     return render_template('signup.html')
     
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global blockData
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Use cipher() to change password to ciphertext
        password = cipher(password, 2)

        blockData = {
            'username': username,
            'email': email,
            'password': password
        }
        
        
        return redirect('/signin')
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global blockData
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Use decipher() to change blockData['password] to plaintext before compairision and store it in painPassword variable
        plainPassword = decipher(blockData['password'], 2)

        # Compair the plainPassword with password instead of blockData['password']
        if blockData['username'] == username and plainPassword == password:
                    return render_template('profile.html', block= blockData)

        return "Invalid credentials!"
    return render_template('signin.html')

capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

def cipher(plaintext, n):
    global  capitalLetters, lowerLetters, numbers
    cipherText = ''

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            cipherText += numbers[(currentPosition + n ) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            cipherText += lowerLetters[(currentPosition + n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            cipherText += capitalLetters[(currentPosition + n) % 26] 
        else:
            cipherText += char

    return cipherText
        
def decipher(ciphertext, n):
    global capitalLetters, lowerLetters, numbers
    plaintext = ""
    # Loop through each char in the ciphertext
    for char in ciphertext:
        # Check if character is present numbers list
        if char in numbers:
            # Get current position of the character in numbers list
            currentPosition = numbers.find(char)
            # Calculate new number as numbers[(currentPosition - n) % 10] and add it to plaintext
            plaintext += numbers[(currentPosition - n) % 10]
        # Check if character is present lowerLetters list    
        elif char in lowerLetters:
            # Get current position of the character in lowerLetters list
            currentPosition = lowerLetters.find(char)
            # Calculate new number as numbers[(currentPosition - n) % 26] and add it to plaintext
            plaintext += lowerLetters[(currentPosition - n )% 26] 
        # Check if character is present capitalLetters list    
        elif char in capitalLetters:
            # Get current position of the character in capitalLetters list
            currentPosition = capitalLetters.find(char)
            # Calculate new number as numbers[(currentPosition - n) % 26] and add it to plaintext
            plaintext += capitalLetters[(currentPosition - n) % 26] 
        # else add the char to plaintext directly
        else:
            plaintext += char

    # Returm the plaintext
    return(plaintext)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)