from config_mod import MEASURE_NORMAL_COLOR, MEASURE_MEDI_COLOR, MEASURE_HIGH_COLOR
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

