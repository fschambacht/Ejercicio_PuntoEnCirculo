import math

def point_in_cirle(x_2, y_2, radius_circle, x_1=0, y_1=0):
    distance = math.sqrt((x_2-x_1)**2+(y_2-y_1)**2)
    if radius_circle >= distance:
        return f'point in {x_2, y_2} is inside the circle with a distance of border {radius_circle-distance}'
    return f'point in {x_2, y_2} is outside the circle with extra distance to border {distance-radius_circle}'

if __name__ == '__main__':
    x_1 = float(input('Enter the point x of circle: '))
    y_1 = float(input('Enter the point y of circle: '))
    radius_circle = float(input('Enter the radio of circle: '))
    x_2 = float(input('Enter the point x: '))
    y_2 = float(input('Enter the point y: '))
    print(point_in_cirle(x_2, y_2, radius_circle, x_1, y_1))
