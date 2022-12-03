from flask import Flask
from utils import get_by_pk, get_all, get_by_skill

app = Flask(__name__)

@app.route("/")
def start_page():
    candidates = get_all()
    page = '<br>'
    for candidate in candidates:
        page += candidate['name'] + '<br>'
        page += candidate['position'] + '<br>'
        page += candidate['skills'] + '<br>'
        page += '<br>'
    return f'<pre> {page} <pre>'


@app.route("/candidates/<int:pk>")
def candidates_page(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return "Такого у нас нет :D"

    url = candidate['picture']
    page = '<br>'
    page += f"<img src='{url}'>" + '<br>'
    page += candidate['name'] + '<br>'
    page += candidate['position'] + '<br>'
    page += candidate['skills'] + '<br>'
    page += '<br>'

    return f"<pre> {page} <pre>"


@app.route("/skills/<x>")
def skills_page(x):
    candidates = get_by_skill(x)
    page = '<br>'
    for candidate in candidates:
        page += candidate['name'] + '<br>'
        page += candidate['position'] + '<br>'
        page += candidate['skills'] + '<br>'
        page += '<br>'
        return f'<pre> {page} <pre>'


if __name__ == "__main__":
    app.run()