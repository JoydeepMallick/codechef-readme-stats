import requests
from bs4 import BeautifulSoup

def get_codechef_stats(username):
    url = f"https://www.codechef.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "User not found"}

    soup = BeautifulSoup(response.text, 'html.parser')

    # (Testing purpose only) Print the entire HTML in a seperate text file
    with open("./output_soup.html", "w") as file:
        file.write(str(soup.prettify()))

    try:
        # Find name of current user
        actual_name = soup.find('h1', class_='h2-style').text.strip()
        print("Actual Name:", actual_name)
        
        # Find rank of current user
        global_rank = soup.find('a', href="/ratings/all").text.strip()
        print("Global Rank:", global_rank)
        country_rank = soup.find('a', href=lambda href: href and "/ratings/all?filterBy=Country" in href).text.strip()
        print("Country Rank:", country_rank)

        # Find the current rating of user
        current_rating = soup.find('div', class_='rating-number').text.strip()
        # Join all digits found in the text
        current_rating = ''.join(filter(str.isdigit, current_rating))
        print("Current Rating:", current_rating)

        # Find codechef username
        codechef_username = username
        print("CodeChef username:", codechef_username)

        # Find division of user
        division = None
        rating_header_section = soup.find('div', class_='rating-header text-center')
        all_divs = rating_header_section.find_all('div')
        for div in all_divs:
            if not div.get('class') and "Div" in div.text.strip():
                div_text = div.text.strip()
                division = div_text.replace("Div ", "")[1:-1]
                break
        print("Division:", division)

        # Find the rating-star section and count the number of stars
        rating_stars_section = soup.find('div', class_='rating-star')
        stars = len(rating_stars_section.find_all('span'))
        print("Stars:", stars)
        
        # Find the highest rating value
        highest_rating_section = soup.find('small', string=lambda x: x and "Highest Rating" in x)
        highest_rating = highest_rating_section.text.strip().split()[-1][:-1]  # Extract the numeric value
        print("Highest Rating:", highest_rating)

        # Extract number of problems solved from badges section
        section = soup.find('section', class_='rating-data-section problems-solved')
        h3_in_section = section.find_all('h3')
        

        problems_solved = None
        for h3 in h3_in_section:
            h3_content = h3.text.strip()
            if "Total Problems Solved:" in h3_content:
                problems_solved = h3_content.replace("Total Problems Solved: ", "").strip()
                break
        print("Problems Solved:", problems_solved)       
        

    except AttributeError:
        return {"error": "Unable to parse user data"}

    return {
        "codechef_url" : url,
        "actual_name": actual_name,
        "codechef_username": codechef_username,
        "global_rank": global_rank,
        "country_rank": country_rank,
        "division": division,
        "current_rating": current_rating,
        "stars": stars,
        "highest_rating" : highest_rating,
        "problems_solved" : problems_solved,
    }

# Testing purpose
if __name__ == "__main__":
    # test users
    users = ['joy2022', 'joy202323223','jwpassion1', 'kdu_1','maroonrk']
    username = users[2]
    print(get_codechef_stats(username))
