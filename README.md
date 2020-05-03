# web-scraping-challenge
Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## What it does?

*  Use Splinter to navigate through sites and Beautiful Soup to scrape latest mars information from web pages below:
   * [NASA Mars News Site](https://mars.nasa.gov/news/)
   * [JPL Mars Space Images](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
   * [Latest Mars weather tweet](https://twitter.com/marswxreport?lang=en)
   * [Mars Facts](https://space-facts.com/mars/)
   * [High resolution images for each of Mar's hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
  
* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

## Preperation

### Install dependencies below
* [pandas](https://pandas.pydata.org)
* [Matplotlib](https://matplotlib.org)
* [Jupyter Notebook](https://jupyter.org/install)
* [numpy](https://numpy.org) 
* [SciPy](https://www.scipy.org/install.html)
* [SQLAlchemy](https://pypi.org/project/SQLAlchemy)
* [Flask](https://pypi.org/project/Flask)
* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo)
* [lxml](https://pypi.org/project/lxml)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4)
* [MongoDB](https://docs.mongodb.com/guides/server/install)
* [Jinja2](https://pypi.org/project/Jinja2)
* [splinter](https://pypi.org/project/splinter)


## How to execute?

### Executing jupyter notebook for web scrapping

```
git clone https://github.com/prerak-patel/web-scraping-challenge.git
cd web-scraping-challenge/Mission_to_Mars
jupyter notebook
Click and Run the mission_to_mars.ipynb
```

### Executing Flask app to render scrapped data to an HTML

```
cd web-scraping-challenge/Mission_to_Mars
python app.py
```

