from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
@app.route('/form')
def homepae():
    return 'hello'


if __name__=="__main__":
   app.run(debug=True)