from __future__ import division
#collecting values
Xa = float(raw_input("Xa = "))
Ya= float(raw_input("Ya = "))
Xb = float(raw_input("Xb = "))
Yb = float(raw_input("Yb = "))
#cacul Y
caculY = float(Yb) - float(Ya)
#Cacul X
caculX = float(Xb) - float(Xa)
#Show result
m= float(caculY) / float(caculX)
print "The result as a fraction is: %s / %s" %(caculY,caculX)
print "The result as a number is:  %s" %(m)

#calculation of the intercept 
p = float(Yb) - (float(m)*float(Xb))
print "the intercept is : %s" %(p)
print "the equation of the line is y= %sx + %s" %(m,p)
