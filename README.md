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

2. `image_gen.py` : Uses drawsvg to generate an svg image and make it self containing and not referencing any other image using base64.

3. `app.py` : runs a server to generate svg image from imported modules and then convert it to png before serving the user.

## How it will look on your system 

### If valid user exists

```markdown
![CodeChef Stats](https://codechef-readme-stats.onrender.com/{your_codechef_username}?v=1)
```

### <span style="color:red">NOTE</span>

**Please do not forget to type the section** `....?v=1` since its essential **force cache refresh in github** to display images else sometimes images are not loaded as intended😐 Learnt it the hard way debugging!!!



Assume user is **joy2022** so I will type the following :-

```markdown
![CodeChef Stats](https://codechef-readme-stats.onrender.com/joy2022?v=1)
```


and output will be :-

![CodeChef Stats](https://codechef-readme-stats.onrender.com/joy2022?v=1)

Assume if user is **maroonrk** then output will be
```markdown
![CodeChef Stats](https://codechef-readme-stats.onrender.com/maroonrk?v=1)
```

![CodeChef Stats](https://codechef-readme-stats.onrender.com/maroonrk?v=1)



### If username does not exists
then it will look something like this as shown below:-

![CodeChef Stats](https://codechef-readme-stats.onrender.com/jfsdkfdsdkfsfh?v=1)


## Want to make your badge redirect people to your profile? 

Try this:

```markdown
[![CodeChef Stats](https://codechef-readme-stats.onrender.com/{your_codechef_username}?v=1)](https://www.codechef.com/users/{your_codechef_username})
```



⚠️THE ABOVE HAVE BEEN TESTED IN Python 3.12.4 and 3.11.3 in Conda Environment and all dependencies listed in requirements.txt have been installed via pip.
