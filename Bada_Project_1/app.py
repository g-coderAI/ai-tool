from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)


def generate_output(choice, text):
    if choice == "1":
        return f"Dear Client,\n\n{text}\n\nBest regards"

    elif choice == "2":
        return f"Title: Amazing Video\n\nIntro:\n{text}\n\nOutro: Thanks for watching!"

    elif choice == "3":
        return f"Name: Your Name\nSkills:\n{text}\nExperience: ..."

    else:
        return "Invalid option"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        choice = request.form.get("choice")
        text = request.form.get("content")

        result = generate_output(choice, text)

    return render_template("index.html", result=result)

@app.route("/download", methods=["POST"])
def download():
    content = request.form.get("content")

    file = io.BytesIO()
    file.write(content.encode("utf-8"))
    file.seek(0)

    return send_file(
        file,
        as_attachment=True,
        download_name="output.txt",
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(debug=True)
    