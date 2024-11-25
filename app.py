from flask import Flask, render_template
import sqlite3

app = Flask(__file__)
database = sqlite3.connect("database.db", check_same_thread=False)

database.execute(f'''CREATE TABLE IF NOT EXISTS "TOTAL_REQUESTS" (
                     TOTAL_REQUESTS     INT
);''')
database.execute(f'INSERT INTO TOTAL_REQUESTS (TOTAL_REQUESTS) VALUES (0);')
database.commit()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html"), 200

@app.route("/HIT")
def hit():
    database.execute(f'UPDATE TOTAL_REQUESTS SET TOTAL_REQUESTS=TOTAL_REQUESTS+1;')
    database.commit()

    return "Sup!", 200

@app.route("/total_requests")
def total_requests():
    total_requests = database.execute('SELECT TOTAL_REQUESTS FROM TOTAL_REQUESTS;').fetchone()[0]
    
    return {"total_requests": total_requests}, 200

@app.route("/reset")
def reset_stats():
    database.execute(f'UPDATE TOTAL_REQUESTS SET TOTAL_REQUESTS=0;')
    database.commit()

    return "Done!", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
