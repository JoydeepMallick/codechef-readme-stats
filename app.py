from flask import Flask, Response
import codechef_data_extractor as cde
import image_gen as ig
import os

app = Flask(__name__)

# Configure static folder (adjust based on your project structure)
app.config['STATIC_FOLDER'] = 'static'

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
        print(svg)
    
    return Response(svg.as_svg(), mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=True)
