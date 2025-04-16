


from test import virtualTest


while True:
    try:
        x = input('input ::: ')
        if (x == 'run'):
            print("==================================++++++++++++====================================")
            print("==================================++++++++++++====================================")
            mainTest = virtualTest()
            y = int(input('how many virtual users? :::'))
            print("==================================++++++++++++====================================")
            print("==================================++++++++++++====================================")
            if (y % 10 != 0):
                print('wrong input , please enter number value')
            mainTest.startTheScript(y)
    except Exception as e:
        print('                                             ======== ERROR ========                                    ')
        print(   f"                                  {e}                                                        "  )