#collecting values
Ya= raw_input("Ya = ")
Yb = raw_input("Yb = ")
Xa = raw_input("Xa = ")
Xb = raw_input("Yb = ")
#cacul Y
caculY = ( int(Yb) - int(Ya) )
#Cacul X
caculX =  ( int(Xb) - int(Xa) )
#Show result
print "The result as a fraction is: %s / %s" %(caculY,caculX)
#request if we want to Integer division
DivEntier = raw_input ("do you want the result to an integer division ? Yes/No : ")
print str(DivEntier)
#into tiny
DivEntier_mini= DivEntier.lower()

#cacul result in integer division
if "yes" in  DivEntier_mini:
        cacul = ( int(Yb) - int(Ya) ) / ( int(Xb) - int(Xa) )

        print "The result is : %s" %(cacul)
else:
        print "It's OK"
