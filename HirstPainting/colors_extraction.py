import colorgram

colors = colorgram.extract('hirst.jpg',30)

# colors.sort(key = lambda c: c.hsl.h)
colors.sort(key = lambda c: c.rgb.r)

def colors_list():
    colors_list = []
    for color in colors:
        colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return colors_list

generated_colors = colors_list()

print(generated_colors)



# print(f'{color.rgb},{color.hsl}')
# color.rgb[0] = red