from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"

@app.route('/index')
def mission_slogan():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    promotion_text = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return "<br>".join(promotion_text)

@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
<html>
<head>
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.jpg')}"
           alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она какая, красная планета.</p>
</body>
</html>'''

@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
<html>
<head>
    <title>Колонизация Марса</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
    <div class="container">
        <h1 class="mt-4">Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/MARS.jpg')}" 
             alt="здесь должна была быть картинка, но не нашлась" 
             class="img-fluid mb-3">
        <div class="promotion-text">
            <h2 class="blue">Человечество вырастает из детства.</h2>
            <h2 class="green">Человечеству мала одна планета.</h2>
            <h2 class="grey">Мы сделаем обитаемыми безжизненные пока планеты.</h2>
            <h2 class="yellow">И начнем с Марса!</h2>
            <h2 class="red">Присоединяйся!</h2>
        </div>
    </div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')