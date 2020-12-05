#Average7.py
#   Compute the average of numbers listed in ma file.
#   Works with multiple numbers on a line.

def main():
    fileName= input("What file are the numbfers in ?")
    infile=open(fileName,'r')
    sum=0.0
    count=0
    line = infile.readline()
    while line!="":
        #update sum and count for values in line
        for xStr in line.split(","):
            sum=sum + float(xStr)
            count=count+1
        line = infile.readline()
    print("\n The average of the numbers is",sum/count)

main()
