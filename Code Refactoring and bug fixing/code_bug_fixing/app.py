from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
notes = []
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'add_note' in request.form:
            note = request.form.get("note")
            notes.append(note)
            return redirect(url_for('index'))
    return render_template("home.html", notes=notes)
@app.route('/delete/<int:note_index>', methods=["POST"])
def delete(note_index):
    if request.method == "POST":
        del notes[note_index]
        return redirect(url_for('index')) 
@app.route('/edit/<int:note_index>', methods=["GET", "POST"])
def edit(note_index):
    if request.method == "POST":
        edited_note = request.form.get("edited_note")
        notes[note_index] = edited_note
        return redirect(url_for('index')) 
    return render_template("edit.html", note_index=note_index, note=notes[note_index])
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
