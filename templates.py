
import requests
import time


class templates:
    
    def __init__(self):
        self.url = 'https://test.khanetala.ir/v1/main'
        
        self.errors = []
        self.counter = []
        self.allResponseTimes = 0



    def _requests(self , url , method):
        if method == 'post':
            pass
            
        elif method == 'get':
            pass
        
        elif method == 'put':
            pass


    ### getting otp template
    def getOtp(self , number): 
        body = {"phoneNumber" : number}
        otpResponse = requests.post('https://test.khanetala.ir/v1/main/otp' , json = {"phoneNumber" : number})
        time.sleep(1)
        print(f'response of otp for user {number} ::: {otpResponse} , {otpResponse.elapsed.total_seconds()}')
        # print('its here ' , otpResponse)        
        responseTime = otpResponse.elapsed.total_seconds()
        self.allResponseTimes += float(responseTime)
        status = otpResponse.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : number,
                "request" : "getting otp",
                "status" : status,
                "responseTime" : responseTime,
                "data" : otpCode['data'] if (status == 200 or status == 201) else 0
            }
            return result
        else:
            otpCode = otpResponse.json()
            result = {
                "user" : number,
                "request" : "getting otp",
                "status" : status,
                "responseTime" : responseTime,
                "data" : otpCode['data'] if (status == 200 or status == 201) else 0
            }
            return result
    
    
    ## verifyOtp template
    def verifyOtp(self , number , otp):
        body = {"phoneNumber" : number, "otp" : otp}
        verifyOtpRespons = requests.post('https://test.khanetala.ir/v1/main/verifyOtp' , json = {"phoneNumber" : number, "otp" : otp})
        time.sleep(1)
        print(f'response of verifyOTP for user {number} ::: {verifyOtpRespons} , {verifyOtpRespons.elapsed.total_seconds()}')
        responseTime = verifyOtpRespons.elapsed.total_seconds()
        self.allResponseTimes += float(responseTime)
        status = verifyOtpRespons.status_code
        self.counter.append(status)
        
        if (status != 200 and status!=201):
            result = {
                "user" : number,
                "request" : "verify otp",
                "status" : status,
                "responseTime" : responseTime,
            }
            return result
        
        
        else:            
            verifyRespone = verifyOtpRespons.json()
            # print(verifyRespone)
            result = {
                "user" : number,
                "request" : "verify otp",
                "status" : status,
                "responseTime" : responseTime,
                "data" : verifyRespone if (status == 200 or status == 201) else 0
            }
            return result
    
    
    
    def identify(self , phoneNumber , birthDate , nationalCode):
        identityRespons = requests.post('https://test.khanetala.ir/v1/main/identify' , json = {"phoneNumber" : phoneNumber, "birthDate" : birthDate , "nationalCode" : nationalCode})
        time.sleep(1)
        responseTime = identityRespons.elapsed.total_seconds()
        print(f'response of identity for user {phoneNumber} ::: {identityRespons} , {identityRespons.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = identityRespons.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "verify otp",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        
        else:            
            identitRespone = identityRespons.json()
            result = {
                "user" : phoneNumber,
                "request" : "verify otp",
                "status" : status,
                "responseTime" : responseTime,
                "data" : identitRespone if (status == 200 or status == 201) else 0
            }
            return result
    
    
    
    def createCart(self , cardNumber , token , phoneNumber):
        createCart = requests.post('https://test.khanetala.ir/v1/main/createCart' , headers = {'authorization' : f"Bearer {token}"} ,json = {"cardNumber" : cardNumber})
        time.sleep(1)
        responseTime = createCart.elapsed.total_seconds()
        print(f'response of createCart for user {cardNumber} ::: {createCart} , {createCart.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = createCart.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "createCart",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            createCartRespone = createCart.json()
            result = {
                "user" : phoneNumber,
                "request" : "createCart",
                "status" : status,
                "responseTime" : responseTime,
                "data" : createCartRespone if (status == 200 or status == 201) else 0
            }
            return result
        
        
        
        
    def profile(self , token , phoneNumber):
        getProfile = requests.get('https://test.khanetala.ir/v1/query/profile' , headers = {'authorization' : f"Bearer {token}"})
        time.sleep(1)
        responseTime = getProfile.elapsed.total_seconds()
        print(f'response of getProfile for user {phoneNumber} ::: {getProfile} , {getProfile.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = getProfile.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "getProfile",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            getProfileRespone = getProfile.json()
            result = {
                "user" : phoneNumber,
                "request" : "getProfile",
                "status" : status,
                "responseTime" : responseTime,
                "data" : getProfileRespone if (status == 200 or status == 201) else 0
            }
            return result
    
    
      
    def depositTransAction(self , token , phoneNumber):
        deposit = requests.post('https://test.khanetala.ir/v1/main/deposit' , headers = {'authorization' : f"Bearer {token}"} , json={"amount" : 1000000000})
        time.sleep(1)
        responseTime = deposit.elapsed.total_seconds()
        print(f'response of deposit for user {phoneNumber} ::: {deposit} , {deposit.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = deposit.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "deposit",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            depositRespone = deposit.json()
            result = {
                "user" : phoneNumber,
                "request" : "deposit",
                "status" : status,
                "responseTime" : responseTime,
                "data" : depositRespone if (status == 200 or status == 201) else 0
            }
            return result
    
    
    
    
    def verifyTransAction(self , token , phoneNumber , authority):
        verifyDeposit = requests.post('https://test.khanetala.ir/v1/main/verifyDeposit' , headers = {'authorization' : f"Bearer {token}"} , json={"status" : "success" , "authority" : authority})
        time.sleep(1)
        responseTime = verifyDeposit.elapsed.total_seconds()
        print(f'response of verifyDeposit for user {phoneNumber} ::: {verifyDeposit} , {verifyDeposit.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = verifyDeposit.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "verifyDeposit",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            verifyDepositRespone = verifyDeposit.json()
            result = {
                "user" : phoneNumber,
                "request" : "verifyDeposit",
                "status" : status,
                "responseTime" : responseTime,
                "data" : verifyDepositRespone if (status == 200 or status == 201) else 0
            }
            return result
    
    
    
    def buyGold(self , token , phoneNumber ):
        buyGold = requests.post('https://test.khanetala.ir/v1/main/createTransaction' , headers = {'authorization' : f"Bearer {token}"} , json={"goldPrice" : 7500000, "goldWeight" : 5 , "type" : "buy" , "totalPrice" : 5*7500000})
        time.sleep(1)
        responseTime = buyGold.elapsed.total_seconds()
        print(f'response of buyGold for user {phoneNumber} ::: {buyGold} , {buyGold.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = buyGold.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "buyGold",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            buyGoldRespone = buyGold.json()
            result = {
                "user" : phoneNumber,
                "request" : "buyGold",
                "status" : status,
                "responseTime" : responseTime,
                "data" : buyGoldRespone if (status == 200 or status == 201) else 0
            }
            return result
        
        
        
    
    def sellGold(self , token , phoneNumber ):
        sellGold = requests.post('https://test.khanetala.ir/v1/main/createTransaction' , headers = {'authorization' : f"Bearer {token}"} , json={"goldPrice" : 7500000, "goldWeight" : 2 , "type" : "sell" , "totalPrice" : 2*7500000})
        time.sleep(1)
        responseTime = sellGold.elapsed.total_seconds()
        print(f'response of sellGold for user {phoneNumber} ::: {sellGold} , {sellGold.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = sellGold.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "sellGold",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            sellGoldRespone = sellGold.json()
            result = {
                "user" : phoneNumber,
                "request" : "sellGold",
                "status" : status,
                "responseTime" : responseTime,
                "data" : sellGoldRespone if (status == 200 or status == 201) else 0
            }
            return result
        
        
    def completeBuyTransaction(self , token , phoneNumber , invoiceId):
        completBuy = requests.post('https://test.khanetala.ir/v1/main/completeBuy' , headers = {'authorization' : f"Bearer {token}"} , json={"invoiceId" : invoiceId , "isFromWallet" : False})
        time.sleep(1)
        responseTime = completBuy.elapsed.total_seconds()
        print(f'response of completBuy for user {phoneNumber} ::: {completBuy} , {completBuy.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = completBuy.status_code
        # print('after completed buy >>>' , completBuy.json())
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "completBuy",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            completBuyRespone = completBuy.json()
            result = {
                "user" : phoneNumber,
                "request" : "completBuy",
                "status" : status,
                "responseTime" : responseTime,
                "data" : completBuyRespone if (status == 200 or status == 201) else 0
            }
            return result
        
        
        
        
        
    def completeSellTransaction(self , token , phoneNumber , invoiceId):
        completeSell = requests.post('https://test.khanetala.ir/v1/main/completeSell' , headers = {'authorization' : f"Bearer {token}"} , json={"invoiceId" : invoiceId })
        time.sleep(1)
        responseTime = completeSell.elapsed.total_seconds()
        print(f'response of completeSell for user {phoneNumber} ::: {completeSell} , {completeSell.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = completeSell.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "completeSell",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            completeSellRespone = completeSell.json()
            result = {
                "user" : phoneNumber,
                "request" : "completeSell",
                "status" : status,
                "responseTime" : responseTime,
                "data" : completeSellRespone if (status == 200 or status == 201) else 0
            }
            return result
        
        
    
    
    def verifyBuyGold(self , token , phoneNumber , authority):
        veirfyBuyGold = requests.post('https://test.khanetala.ir/v1/main/verifyTransaction' , headers = {'authorization' : f"Bearer {token}"} , json={"status" : "success" , "authority" : authority})
        time.sleep(1)
        responseTime = veirfyBuyGold.elapsed.total_seconds()
        print(f'response of veirfyBuyGold for user {phoneNumber} ::: {veirfyBuyGold} , {veirfyBuyGold.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = veirfyBuyGold.status_code
        self.counter.append(status)
        if (status != 200 and status != 201):
            result = {
                "user" : phoneNumber,
                "request" : "veirfyBuyGold",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            veirfyBuyGoldRespone = veirfyBuyGold.json()
            result = {
                "user" : phoneNumber,
                "request" : "veirfyBuyGold",
                "status" : status,
                "responseTime" : responseTime,
                "data" : veirfyBuyGoldRespone if (status == 200 or status == 201) else 0
            }
            return result
        
        
    def getTransACtions(self , token , phoneNumber):
        getWallet = requests.get('https://test.khanetala.ir/v1/query/wallet' , headers = {'authorization' : f"Bearer {token}"})
        time.sleep(1)
        responseTime = getWallet.elapsed.total_seconds()
        print(f'response of getWallet for user {phoneNumber} ::: {getWallet} , {getWallet.elapsed.total_seconds()}')
        self.allResponseTimes += float(responseTime)
        status = getWallet.status_code
        self.counter.append(status)
        if (status != 200 and status!=201):
            result = {
                "user" : phoneNumber,
                "request" : "getWallet",
                "status" : status,
                "responseTime" : responseTime,
                "data" : 0
            }
            return result
        else:            
            getWalletRespone = getWallet.json()
            result = {
                "user" : phoneNumber,
                "request" : "getWallet",
                "status" : status,
                "responseTime" : responseTime,
                "data" : getWalletRespone if (status == 200 or status == 201) else 0
            }
            return result
    
    
    
    
    ## getter the requests counter>>>>>>>><<<<<<<<<<<<<<
    def getResult(self):
        return [self.counter , self.allResponseTimes]
    

    