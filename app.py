from flask import Flask

app = Flask(__name__, static_url_path='/assets', static_folder='./assets')


@app.route('/')
def hello_world():
    return open('index.html').read()

@app.route('/asserts/<path:path>')
def send_assets(path):
    print(f'asserts/{path}')
    return open(f'asserts/{path}', 'rb').read()


if __name__ == '__main__':
    app.run(debug=True)


