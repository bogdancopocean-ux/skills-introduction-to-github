from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .container {
                text-align: center;
                background: white;
                padding: 60px 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                animation: fadeIn 0.8s ease-in;
            }
            h1 {
                color: #333;
                font-size: 3.5em;
                margin-bottom: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            p {
                color: #666;
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            .emoji {
                font-size: 4em;
                margin: 20px 0;
                animation: bounce 2s infinite;
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(-20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes bounce {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-20px);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">👋</div>
            <h1>Hello, World!</h1>
            <p>Welcome to your fancy Flask application</p>
        </div>
    </body>
    </html>
    """
    return html


@app.route('/countries')
def countries():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Country Photos</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f3f4f6;
                padding: 40px;
                color: #111827;
            }
            .wrap {
                max-width: 1100px;
                margin: 0 auto;
            }
            h1 {
                text-align: center;
                margin-bottom: 16px;
                font-size: 2.4rem;
            }
            p.lead {
                text-align: center;
                color: #6b7280;
                margin-bottom: 28px;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 18px;
            }
            .card {
                background: white;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
            }
            .card img {
                width: 100%;
                height: 160px;
                object-fit: cover;
                display: block;
            }
            .card .meta {
                padding: 12px 14px;
            }
            .meta h3 {
                margin: 0 0 6px 0;
                font-size: 1.05rem;
            }
            .meta p {
                margin: 0;
                color: #6b7280;
                font-size: 0.95rem;
            }
            .back {
                display: inline-block;
                margin: 20px 0 8px;
                text-decoration: none;
                color: #4f46e5;
            }
        </style>
    </head>
    <body>
        <div class="wrap">
            <a class="back" href="/">← Back to Home</a>
            <h1>Country Photos</h1>
            <p class="lead">A small gallery of country photos (sourced from Wikimedia Commons)</p>

            <div class="grid">
                <div class="card">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/Statue_of_Liberty_7.jpg" alt="Statue of Liberty, USA">
                    <div class="meta">
                        <h3>United States</h3>
                        <p>Statue of Liberty, New York City</p>
                    </div>
                </div>

                <div class="card">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tour_Eiffel_Wikimedia_Commons.jpg" alt="Eiffel Tower, France">
                    <div class="meta">
                        <h3>France</h3>
                        <p>Eiffel Tower, Paris</p>
                    </div>
                </div>

                <div class="card">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Mount_Fuji_from_Yamanakako.jpg" alt="Mount Fuji, Japan">
                    <div class="meta">
                        <h3>Japan</h3>
                        <p>Mount Fuji</p>
                    </div>
                </div>

                <div class="card">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/66/Cristo_Redentor_-_Rio_de_Janeiro%2C_Brasil.jpg" alt="Christ the Redeemer, Brazil">
                    <div class="meta">
                        <h3>Brazil</h3>
                        <p>Christ the Redeemer, Rio de Janeiro</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)