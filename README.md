# CodeChef Readme Stats

Similar to what Codeforces Readme stats does. 

### Requirements
- requests
- beautifulsoup4
- drawsvg
- Flask

## Main folders and files structure :-

```
codechef_readme_stats/
│
├── codechef_data_extractor.py
├── image_gen.py
├── app.py
├── static/
│   ├── One_chef's_hat.png
│   ├── codechef_logo.png
│   └── Chef_not_found.png
├── requirements.txt
└── README.md

```

As off now :-

1. `codechef_data_extractor.py` : uses BeautifulSoup to extract data from CodeChef profile static HTML page

2. `image_gen.py` : Uses Svg_write to generate an image

3. `app.py` : runs a server to view the image

### How it will look on your system 
Assume user is **joy2022**

```
![](your_codechef_username)
```
![](http://127.0.0.1:5000/joy2022)