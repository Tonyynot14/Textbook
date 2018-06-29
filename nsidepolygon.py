# Tony Wade
# 6/29/2018
# A test file for the nsidepolygonclass file. all seems to work

from nsidepolygonclass import RegularPolygon


polygon = RegularPolygon(5,7)

print(polygon.getArea(), polygon.getPerimeter())