try:
    age=12
    if age<18:
        raise ValueError("age for voting is min 18")
    else:
        print("eligible for vote")
except ValueError as e:
    print(str(e))

    #a=10
    #b=90
    #c=a/b
    #print(c)

#except ZeroDivisionError as e:
   # print("division not possible by zero"+str(e))
except:
    print("exception occured")
else:
    print("executed successfully")
finally:
    print("harman ltd")
