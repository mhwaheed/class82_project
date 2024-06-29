Cipher and Decipher the Username and Password
=============================================

In this activity, you will learn to cipher and decipher the username and the password.


<img src= "https://media.slid.es/uploads/1525749/images/10631740/pcp.gif" width = "480" height = "320">


Follow the given steps to complete this activity:
1. Create div for ciphered data.

* Open file `app.py`

* Use `cipher()` to change password to ciphertext in `signup()` function.

    `password = cipher(password, 2)`

*  Use `decipher()` to change `blockData['password]` to plaintext before compairision and store it in `painPassword` variable.

    `plainPassword = decipher(blockData['password'], 2)`


* Compare the `plainPassword` with `password` instead of `blockData['password']`.

    `if blockData['username'] == username and plainPassword == password:`

* return to the `profile` page and pass `blockData` to it.

    `return render_template('profile.html', block= blockData)`


* Save and run the code to check the output.

