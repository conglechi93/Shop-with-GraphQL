from config.settings import app


@app.route('/')
def hello():
    return 'My First API !!'


if __name__ == '__main__':
    app.run()
