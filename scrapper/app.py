from flask import Flask, request, render_template
from scraper.scraper import scrape_product

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    product = scrape_product(url)
    return render_template('result.html', product=product)

@app.route('/compare', methods=['POST'])
def compare():
    url1 = request.form['url1']
    url2 = request.form['url2']
    product1 = scrape_product(url1)
    product2 = scrape_product(url2)
    return render_template('comparison.html', product1=product1, product2=product2)

if __name__ == '__main__':
    app.run(debug=True)
