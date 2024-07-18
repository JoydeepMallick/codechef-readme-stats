from flask import Flask, Response, send_file
import codechef_data_extractor as cde
import image_gen as ig
import os
import io
import cairosvg

app = Flask(__name__)

# Configure static folder (adjust based on your project structure)
app.config['STATIC_FOLDER'] = 'static'

# Show this when you are in root
@app.route('/')
def root():
    return """
    <html>
        <head>
            <title>CodeChef Readme Stats</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                }
                .container {
                    display: inline-block;
                    text-align: left;
                    border: 2px solid #ddd;
                    padding: 20px;
                    border-radius: 10px;
                }
                h1 {
                    color: #ff5722;
                }
                p {
                    font-size: 18px;
                }
                .example {
                    background-color: #f9f9f9;
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }
                .github-link {
                    text-align: center;
                    margin-top: 20px;
                }
                .github-link a {
                    display: inline-block;
                    text-decoration: none;
                    color: #333;
                    font-size: 20px;
                }
                .github-link img {
                    width: 24px;
                    height: 24px;
                    vertical-align: middle;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to CodeChef Readme Stats! 🍽️</h1>
                <p>Type your CodeChef username <b>after the URL</b> in the address bar above☝️ to see your badge.</p>
                <p>Example: <span class="example"><a href="https://codechef-readme-stats.onrender.com/joy2022">https://codechef-readme-stats.onrender.com/joy2022</a></span></p>
                <p>👨‍🍳 Showcase your CodeChef stats proudly in your GitHub profile! 👩‍🍳</p>
                <p>Nothing to show here at the root😌.</p>

                <p>Oh wait🤚, since you're here, why not take a look at the code on GitHub👇? It's open source BTW😏</p>
                
                <div class="github-link">
                    <a href="https://github.com/JoydeepMallick/codechef-readme-stats" target="_blank">
                        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo"> View on GitHub
                    </a>
                </div>

                <p>Won't mind if you mistakenly press the ⭐ (🥹 means a lot!)</p>
            </div>
        </body>
    </html>
    """

# Show your badge when you visit here
@app.route('/<username>')
def codechef_stats(username):
    stats = cde.get_codechef_stats(username)
    hat_image = os.path.join(app.config['STATIC_FOLDER'], 'One_chef\'s_hat.png')
    if "error" not in stats:
        codechef_logo = os.path.join(app.config['STATIC_FOLDER'], 'codechef_logo.png')
        svg = ig.generate_svg_with_hat(stats, hat_image, codechef_logo)
    else:
        error_image = os.path.join(app.config['STATIC_FOLDER'], 'Chef_not_found.png')
        svg = ig.generate_error_svg(username, hat_image, error_image)

     # convert drawing object to a svg file
    svg = svg.as_svg()
    print(svg)

    # Convert SVG data to PNG format using cairosvg
    png_data = cairosvg.svg2png(bytestring=svg)
    png_io = io.BytesIO(png_data)
    
    return send_file(png_io, mimetype='image/png')
    # return Response(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
