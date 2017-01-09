while True:
    try:
        number = input("Enter a number \n")
        print (number)
        break
    except ValueError:
        print ("try again1")
    except NameError:
        print ("try again2")
    except:
        break
    finally:
        print ("loop complete")
