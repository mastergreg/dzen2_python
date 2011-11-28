from time import strftime
from colors import set_colors,set_normal_color
from config_mod import TIME_COLOR,TIME_BACKGROUND_COLOR
def NOW():
  return set_colors(TIME_COLOR,TIME_BACKGROUND_COLOR)+strftime("%d-%m %H:%M")+set_normal_color()
