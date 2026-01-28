from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CI/CD Status</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #0f172a;
                font-family: Arial, sans-serif;
                color: #e5e7eb;
            }
            .card {
                background: #020617;
                padding: 30px 40px;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            }
            h1 {
                margin-bottom: 10px;
                color: #22c55e;
            }
            button {
                margin-top: 20px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background: #2563eb;
                color: white;
                cursor: pointer;
                font-size: 14px;
            }
            button:hover {
                background: #1d4ed8;
            }
            #time {
                margin-top: 15px;
                font-size: 13px;
                color: #94a3b8;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✅ CI/CD Pipeline Working</h1>
            <p>Flask app deployed successfully.</p>
            <button onclick="showTime()">Show Server Time</button>
            <div id="time"></div>
        </div>

        <script>
            function showTime() {
                const now = new Date();
                document.getElementById("time").innerText =
                    "Client Time: " + now.toLocaleString();
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
