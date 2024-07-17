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

Main files :-

1. `codechef_data_extractor.py` : uses BeautifulSoup to extract data from CodeChef profile static HTML page

2. `image_gen.py` : Uses Svg_write to generate an image

3. `app.py` : runs a server to view the image

## How it will look on your system 

## If valid user exists

```markdown
![](https://codechef-readme-stats.onrender.com/your_codechef_username)
```

Assume user is **joy2022** so I will type the following :-

```
![](https://codechef-readme-stats.onrender.com/joy2022)
```

and output will be :-

![](https://codechef-readme-stats.onrender.com/joy2022)


### If username does not exists
then it will look something like this as shown below:-

![](https://codechef-readme-stats.onrender.com/jfsdkfdsdkfsfh)


## Want to make your badge redirect people to your profile? 

Try this:

```
[![](https://codechef-readme-stats.onrender.com/your_codechef_username)](https://www.codechef.com/users/your_codechef_username)
```


![](http://localhost:5000/joy2022)


⚠️THE ABOVE HAVE BEEN TESTED IN Python 3.12.4 and 3.11.3 in Conda Environment and all dependencies listed in requirements.txt have been installed via pip.
