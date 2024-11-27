s1=int(input("Enter the first speed: "))
s2=int(input("Enter the second speed: "))
s3=int(input("Enter the third speed: "))

avg= (s1+s2+s3)/3

if s1> avg:
    print(f"the first speed: {s1} is greater than the average speed {avg} ")
elif s2> avg:
    print(f"the second speed: {s2} is greater than the average speed {avg} ")
elif s3>avg:
    print(f"the third speed: {s3} is greater than the average speed {avg} ")
else:
    print("The speeds are all equal to average speed")

