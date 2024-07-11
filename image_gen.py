import drawsvg as draw
import codechef_data_extractor as cde

def generate_svg_with_hat(data, image_path, codechef_icon):
    # Create a drawing object
    d = draw.Drawing(400, 500, origin='center', displayInline=False)
    
    # Add the chef hat image as background
    d.append(draw.Image(-200, -250, 400, 500, image_path))

    # Coordinates for text
    y_start = -100
    y_step = 25
    ############################ CodeChef Icon #############################
    d.append(draw.Image(x=-40, y=-190, width=80, height=80, path=codechef_icon))

    ############################ Upper Section #############################
    # Actual Name
    d.append(draw.Text(text=f'Name: {data["actual_name"]}', font_size=20, x=0, y=y_start, center=True, fill='black'))  
    # Username
    y_start += y_step
    d.append(draw.Text(text=f'Username: {data["codechef_username"]}', font_size=20, x=0, y=y_start, center=True, fill='black'))
    
    ############################ Middle Section #############################
    # Global Rank
    y_start += y_step + 10
    d.append(draw.Text(text=f'Global Rank: {data["global_rank"]}', font_size=15, x=0, y=y_start, center=True, fill='black'))
    # Country Rank
    y_start += y_step
    d.append(draw.Text(text=f'Country Rank: {data["country_rank"]}', font_size=15, x=0, y=y_start, center=True, fill='black'))
    # Current Rating
    y_start += y_step
    d.append(draw.Text(text=f'Current Rating: {data["current_rating"]}', font_size=15, x=0, y=y_start, center=True, fill='black'))
    # Division
    y_start += y_step
    d.append(draw.Text(text=f'Division: {data["division"]}', font_size=15, x=0, y=y_start, center=True, fill='black')) 
    # Highest Rating
    y_start += y_step
    d.append(draw.Text(text=f'Highest Rating: {data["highest_rating"]}', font_size=15, x=0, y=y_start, center=True, fill='black')) 
    # Problems Solved
    y_start += y_step
    d.append(draw.Text(text=f'Problems Solved: {data["problems_solved"]}', font_size=15, x=0, y=y_start, center=True, fill='black'))

    ############################ Lower Section #############################
    # Stars
    y_start += y_step + 40
    stars = '★' * int(data["stars"])
    alloted_color = color_picker(data['stars'], data['current_rating'])
    d.append(draw.Text(text=stars, font_size=30, x=0, y=y_start, center=True, fill=alloted_color))
    
    return d


def color_picker(star_count, current_rating):
    # upper bound rating, number of stars needed, alloted color
    # To get more info on the rating system read this -> https://blog.codechef.com/2017/03/09/a-star-studded-rating-system/
    rating_to_stars = [
        (1399, 1, '#4D4356'),# GREY
        (1599, 2, '#18641B'),# GREEN
        (1799, 3, '#2952A3'),# BLUE
        (1999, 4, '#53355C'),# VIOLET
        (2199, 5, '#997300'),# YELLOW OCHRE
        (2499, 6, '#CC6600'),# ORANGE
        (float('inf'), 7, '#A60116')# RED
    ]
    for upper_bound, stars, color in rating_to_stars:
        if int(current_rating) <= upper_bound and int(star_count) == stars:
            return color
    return '#A60116'  # Default case (for legends only LMAO)


def generate_error_svg(username, image_path, error_image_path):
    # Create a drawing object
    d = draw.Drawing(width=400, height=500, origin='center', displayInline=False)
    
    # Add the chef hat image as background
    d.append(draw.Image(x=-200, y=-250, width=400, height=500, path=image_path))

    # Place error image over hat
    d.append(draw.Image(x=-150, y=-200, width=300, height=300, path=error_image_path))

    # Add the error message
    d.append(draw.Text(text=f'Chef was not found.', font_size=20, x=0, y=150, center=True, fill='red'))
    d.append(draw.Text(text="Sorry😒\n can't cook right now", font_size=16, x=0, y=90, center=True, fill='red'))
    
    return d



# # (Testing purpose only)Extracting data for a specific user
# stats = cde.get_codechef_stats("joy2022")

# if "error" not in stats:
#     svg = generate_svg_with_hat(stats, './static/One_chef\'s_hat.png', './static/codechef_logo.png')
#     svg.save_svg('./codechef_stats_with_hat.svg')
#     print("SVG file created successfully.")
# else:
#     print("Error generating SVG, use the image generated instead")
#     svg = generate_error_svg(stats, './static/One_chef\'s_hat.png', './static/Chef_not_found.png')
#     svg.save_svg('./codechef_stats_chef_not_found.svg')