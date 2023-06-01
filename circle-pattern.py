tam = 30
arc_quantity = 50
coord = []
arc_rotation = [0, HALF_PI, PI, PI+HALF_PI, TWO_PI]

def setup():
    size(600, 600)
    fill(0)
    rect_mode(CENTER)
    
#def draw():
    background(240)
    rows = cols = width // tam
    tam_arc = tam -3
    for r in range(rows):
        y = tam * r + tam / 2
        for c in range(cols):
            x = tam * c + tam / 2
            coord.append([x, y])
            no_fill()
            stroke_weight(1)
            stroke(150)
            circle(x, y, tam_arc)

    for a in range(arc_quantity):
        arc_pos = random_int(100, 300)
        stroke(0)
        stroke_weight(3)
        arc(coord[arc_pos][0], coord[arc_pos][1], tam_arc, tam_arc, random_choice(arc_rotation), random_choice(arc_rotation))
        
    
    
    
'''            
            for a in range(r * c):
                stroke_weight(4)
                stroke(0)
                arc(x, y, tam, tam, HALF_PI)
'''