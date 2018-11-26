#Percent Calculator - ipo7.py

outOf = int(25)
mark = int(input("Student: What's my mark on my test?"))
percent = mark / outOf * 100
print("Teacher: " + str(mark) + " out of " + str(outOf))
print("Student: What's " + str(mark) + " out of " + str(outOf) + " in percent form?")
print("Teacher: That would be " + str(percent) + "%.")

if percent > 100:
    print("Student: I think you've made a mistake. I couldn't possibly score a " + str(percent) + "%.")
