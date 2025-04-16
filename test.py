import threading
import time
import requests
import json
import timeit
from templates import templates




class virtualTest :
    
    def __init__(self):        
        self.scenarios = templates()
        self.start = timeit.default_timer()
        self.a=[]
        self.phoneNumber = []
        self.users = []
        self.resaults = {"results" : []}



    def __geProfile(self , token , phone):
        getProf = self.scenarios.profile(token , phone)
        if (getProf['status'] == 200):
            print('user profile get successfully')
        time.sleep(0.5)
        
        
    def _getWallet(self , token , phone):
        getTransACtions = self.scenarios.getTransACtions(token , phone)
        if (getTransACtions['status'] == 200):
            print('user profile get successfully')
        time.sleep(0.5)
        



    ##main function for calling the apis 
    def print_name(self , id):
        user = f'091112121{id+72}'
        cartUSer = f'{user}-6037'
        nationalCode = f'{user}-242'
        birthdate = f'1376/30/05-{user}'
        self.phoneNumber.append(user)
        userVerifyDone = 0
        identification = 0
        token = None
        userProfile = None
        getOtp = self.scenarios.getOtp(user)
        if (getOtp == False):
            print('getting otp requests failed because of some external issued>>>>>')
        self.resaults['results'].append(getOtp)
        if getOtp['data'] !=0 :
            verifyOtp = self.scenarios.verifyOtp(user , getOtp['data'])
            if (getOtp == False):
                print('getting otp requests failed because of some external issued>>>>>')
            self.resaults['results'].append(verifyOtp)
            if (verifyOtp["status"] == 200):
                userVerifyDone = 1

        if (userVerifyDone == 1):
            if (verifyOtp['data']['userVerificationStatus'] == "FAILED"):
                identify = self.scenarios.identify(user , nationalCode=nationalCode , birthDate=birthdate)
                if (identify['status'] == 200):
                    identification =1
                    token = identify['data']['token']
            elif(verifyOtp['data']['userVerificationStatus'] == "SUCCESS"):
                identification =1
                token = verifyOtp['data']['token']
            # print('userVerified >>>>' ,userVerifyDone,identification,token )
        
        if (identification == 1):
            ###profile
            getProf = self.scenarios.profile(token , user)
            if (getProf['status'] == 200):
                userProfile = getProf['data']
                # print(userProfile)
                self._getWallet(token , user)            
                
        # print(userProfile['isHaveBank'])
        if (userProfile['isHaveBank'] == False):
            createCart = self.scenarios.createCart(cartUSer , token , user)
            if (createCart['status'] == 200 or createCart['status'] == 201):
                self.__geProfile(token , user)
                self._getWallet(token , user)            

                # print(f'user {user} create cart successfully')
            else : 
                self.__geProfile(token , user)
                self._getWallet(token , user)            

                # print(f'user {user} did not create cart')
                
        
        
        deposit = self.scenarios.depositTransAction(token , user)
        if deposit['status'] == 200:
            self.__geProfile(token , user)
            self._getWallet(token , user)            
            # print('data issssssss' , deposit['data'])
            verifyDeposti = self.scenarios.verifyTransAction(token , user , deposit['data']['authority'])
            if (verifyDeposti['status'] == 200 or verifyDeposti['status'] ==201):
                self.__geProfile(token , user)
                self._getWallet(token , user)            

                # print(f'verificatiion of deposit done {user}')
            else:
                self.__geProfile(token , user)
                self._getWallet(token , user)            

                # print(f'verification of deposit failed {user}')
        else:
            self.__geProfile(token , user)
            self._getWallet(token , user)            

            # print(f'deposit failed for user {user}')
    
        startBuy = self.scenarios.buyGold(token , user)
        if (startBuy['status'] == 200 or startBuy['status'] == 201):
            self.__geProfile(token , user)
            self._getWallet(token , user)            
            # print(startBuy)
            completeBuyTransaction = self.scenarios.completeBuyTransaction(token , user , startBuy['data']['transactionId'])
            # print('response of completeBuy' , completeBuyTransaction)
            if (completeBuyTransaction['status'] == 200  or completeBuyTransaction['status'] == 201):
                self.__geProfile(token , user)
                self._getWallet(token , user)            
                # print('completeBuyTransaction' , completeBuyTransaction)
                verifyTransaction = self.scenarios.verifyBuyGold(token , user , completeBuyTransaction['data']['invoice']['authority'])
                if (verifyTransaction['status'] == 200  or verifyTransaction['status'] == 201):
                    self.__geProfile(token , user)
                    self._getWallet(token , user)            

                    # print(f'completing buy successfully done! for user {user}')
                    sellGold = self.scenarios.sellGold(token , user)
                    if (sellGold['status'] == 200  or sellGold['status'] == 201):
                        self.__geProfile(token , user)
                        self._getWallet(token , user)            

                        # print(f'start the sell for user {user}')
                        # completSell = self.scenarios.completeSellTransaction(token , user , sellGold['data']['transactionId'])
                        # if (completSell['status'] == 200  or completSell['status'] == 201):
                        #     self.__geProfile(token , user)
                        #     self._getWallet(token , user)            

                        #     # print(f'completing sell for user {user} done!')
                        # else : 
                        #     self.__geProfile(token , user)
                        #     self._getWallet(token , user)            

                            # print(f'completing sell failed for user {user}')
                    else : 
                        self.__geProfile(token , user)
                        self._getWallet(token , user)            

                        # print(f'creating sell transactio for user {user} failed')
                else :
                    self.__geProfile(token , user)
                    self._getWallet(token , user)            

                    # print(f'completing buy failed for user {user}')
            else : 
                self.__geProfile(token , user)
                self._getWallet(token , user)            

                # print(f'completing buy failed for user {user}!')
        else:
            self.__geProfile(token , user)
            self._getWallet(token , user)            

            # print(f'creating transaction for user {user} failed!')
            
        
        
        
        
            
            
        
        





    ###############################################################################################################
    ### start the scenario
    ###############################################################################################################
    def startTheScript(self , count):
        threads = []
        for i in range(count):    
            t = threading.Thread(target=self.print_name, args=(i,))
            t.start()
            threads.append(t)
            
            

        for j in threads:
            j.join()

        stop = timeit.default_timer()

        count = 0
        for i in self.a:
            print(i)
            
        # serialized_data = json.loads(resaults)

        json_object = json.dumps(self.resaults)

        with open("resaut700Users.json" , "w") as f:
            f.write(json_object)


        print('==============================================================================')

        users = self.phoneNumber
        responseTimes = self.scenarios.getResult()[1]
        print(f'test run for {len(users)} virtual users successfull in time :: {responseTimes}')
        print('')
        
        print('==============================================================================')
        print(f'{len(self.resaults.keys())} try for request happened . . .')
        print('')
        
        print('==============================================================================')
        print(f'{len(self.a)} requests done!')


        print('==============================================================================')
        print('==============================================================================')
        print('==============================================================================')


        counter = self.scenarios.getResult()[0]

        success = [x for x in counter if x == 200]
        internalError = [x for x in counter if x >= 500]
        forbidden = [x for x in counter if x == 403]
        unAuthorize = [x for x in counter if x == 401]
        badRequest = [x for x in counter if x == 400]

        print(f'{len(success)} requests 200 status code . . .')
        print ("")
        print(f'{len(internalError)} requests 500 status code internal Error . . .')
        print('')
        print(f'{len(forbidden)} requests 403 status code internal Error . . .')
        print ("")
        
        print(f'{len(unAuthorize)} requests 401 status code internal Error . . .')
        print ("")
        
        print(f'{len(badRequest)} requests 400 status code internal Error . . .')
        print ("")


        print('==============================================================================')
        print('==============================================================================')
        print('==============================================================================')















# response of completSell for user 09111111110
# response of deposit for user 09111111110 