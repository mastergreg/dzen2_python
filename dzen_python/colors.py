from config_mod import MEASURE_NORMAL_COLOR, MEASURE_MEDI_COLOR, MEASURE_HIGH_COLOR
def parse_rgb(color):
    r = int(int(color[1:3],16)*100/256)
    g = int(int(color[3:5],16)*100/256)
    b = int(int(color[5:7],16)*100/256)
    return (r,g,b)

def unparse_rgb(nRGB):
    (newR,newG,newB) = nRGB
    r = "{0:02X}".format(int(newR*256/100))
    if len(r)==1:
        r="0"+r
    g = "{0:02X}".format(int(newG*256/100))
    if len(g)==1:
        g="0"+g
    b = "{0:02X}".format(int(newB*256/100))
    if len(b)==1:
        b="0"+b
    return "#"+r+g+b

def mix_colors(low, high, perc):
    (lowR,lowG,lowB) = low
    (highR,highG,highB) = high
    lowPerc = 100 - perc
    newR = (lowR*lowPerc+highR*perc)/100
    newG = (lowG*lowPerc+highG*perc)/100
    newB = (lowB*lowPerc+highB*perc)/100
    return unparse_rgb((newR,newG,newB))

  

def set_gradient_color(percentage):
    if percentage < 50 :
        colorMix = mix_colors(parse_rgb(MEASURE_NORMAL_COLOR),parse_rgb(MEASURE_MEDI_COLOR),percentage*2)
    else:
        colorMix = mix_colors(parse_rgb(MEASURE_MEDI_COLOR),parse_rgb(MEASURE_HIGH_COLOR),(percentage-50)*2)
    print(colorMix)
    return '^fg('+colorMix+')'


def set_color(color):
    return '^fg('+color+')^bg()'
def set_colors(fbcolor,bgcolor):
    return '^fg('+fbcolor+')^bg('+bgcolor+')'
def set_normal_color():
    return '^fg()^bg()'
def set_measure_color(percentage):
    if (percentage>66):
        return '^fg('+MEASURE_HIGH_COLOR+')'
    elif (percentage>33):
        return '^fg('+MEASURE_MEDI_COLOR+')'
    else:
        return '^fg('+MEASURE_NORMAL_COLOR+')'

