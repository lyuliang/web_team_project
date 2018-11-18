def myprint(s,w1,w2,w3,w4):
    print("#WSUM(%f %s.url  %f %s.keywords %f %s.title %f %s.body) " %(w1,s,w2,s,w3,s,w4,s),end = ' ')


inputs = ["Pearl farming","Green party political views","Controlling type II diabetes","Aspirin cancer prevention",
"Pyramid scheme","Hubble telescope repairs","Airline overbooking","hedge funds fraud protection","Puerto Rico state",
"Scrabble Players"]
w1 = 0.2
w2 = 0.2
w3 = 0.3
w4 = 0.3
for s in inputs:
    l = s.split(' ')
    for w in l:
        myprint(w,w1,w2,w3,w4)
    print()