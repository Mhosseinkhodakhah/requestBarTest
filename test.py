import threading
import time
import requests
import json
import timeit


start = timeit.default_timer()

# def requester(url , method):
#     result = 0
#     while result == 0:
#         match method:
#             case 'get':
#                 requests.get(url)



a=[]
counter = []
users = []
resaults = {}
def print_name(id):
    # if (id == 5):
    #     time.sleep(5)
    users.append(id)
    try:
        print(f'test request start successfully for user/{id}')
        response = requests.get('url')
        a.append(f'user/{id} , {response} in time {response.elapsed.total_seconds()}')
        counter.append(response.status_code)
        response2 = requests.get('url')
        a.append(f'user/{id} => second request ,{response2} in time = > {response2.elapsed.total_seconds()}')
        counter.append(response2.status_code)
        print(f'test request done successfully for user/{id}')
        resaults[f'user/{id}-test1'] = response.json()
        resaults[f'user/{id}-test2'] = response2.json()
        time.sleep(0.5)
    except Exception as e:
        print(e)
        resaults[f'user/{id}-testing'] = f'{e}'
        # print(f'test failed for user/{id} cause :::: {e}') 
        
       
    registerBody = {
    "fullName" : f"test{id}",
    "userName" : f"Test{id}",
    "email" : f"test{id}@gmail.com ",
    "country" : f"test{id}",
    "password" : f"Test@{id}",
    "language" : f"persian",
    "school" : f"shahid{id}"
}   
    try:
        print(f'register request start for user/{id}')
        register = requests.post('url' , json=registerBody)
        a.append(f'user/{id} => register request ,{register} in time = > {register.elapsed.total_seconds()}')
        counter.append(register.status_code)
        token = register.json()['data']['user']['token']
        refreshToken = register.json()['data']['user']['refreshToken']
        print(f'register request done for user/{id}')
        resaults[f'user/{id}-register'] = json.loads(register.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-register'] = f'{e}'
        print(f'register failed for user/{id} cause :::: {e}')
        time.sleep(0.5)
    
    try:
        print(f'checkToken test start for user/{id}')
        checkToken = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => checkToken request ,{checkToken} in time = > {checkToken.elapsed.total_seconds()}')
        counter.append(checkToken.status_code)
        print(f'check token test passed for user/{id}')
        resaults[f'user/{id}-checkToken'] = json.loads(checkToken.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-checkToken'] = f'{e}'
        print(f'checkToken failed for user/{id} cause :::: {e}')  
        time.sleep(0.5) 
        
        
         
    try:
        print(f'getUser request start for user/{id}')
        getUser = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getUser request ,{getUser} in time = > {getUser.elapsed.total_seconds()}')
        counter.append(getUser.status_code)
        print(f'getUser request done for user/{id}')
        resaults[f'user/{id}-getUser'] = json.loads(getUser.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getUser'] = f'{e}'
        print(f'getUser failed for user/{id} cause :::: {e}')    
        time.sleep(0.5)    
        
    try:    
        print(f'getUserPoint request start for user/{id}')
        getUserPoints = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getUserPoints request ,{getUserPoints} in time = > {getUserPoints.elapsed.total_seconds()}')
        counter.append(getUserPoints.status_code)
        print(f'getUserPoint request done for user/{id}')
        resaults[f'user/{id}-getUserPoints'] = json.loads(getUserPoints.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getUserPoints'] = f'{e}'
        print(f'getUserPoint failed for user/{id} cause :::: {e}')   
        time.sleep(0.5)     
        
        
        
    try:
        print(f'getPersianLessons reqeust start user/{id}')
        getpersianlessons = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getpersianlessons request ,{getpersianlessons} in time = > {getpersianlessons.elapsed.total_seconds()}')
        counter.append(getpersianlessons.status_code)
        print(f'getPersianLessons reqeust done user/{id}')
        resaults[f'user/{id}-getpersianlessons'] = json.loads(getpersianlessons.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getpersianlessons'] = f'{e}'
        print(f'getPersianLessons failed for user/{id} cause :::: {e}')
        time.sleep(0.5)
        
    
    try:  
        print(f'getEnglishLessons reqeust start user/{id}')
        getEnglishLesson = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getEnglishLesson request ,{getEnglishLesson} in time = > {getEnglishLesson.elapsed.total_seconds()}')
        counter.append(getEnglishLesson.status_code)
        print(f'getEnglishLessons reqeust done user/{id}')
        resaults[f'user/{id}-getEnglishLesson'] = json.loads(getEnglishLesson.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getEnglishLesson'] = f'{e}'
        print(f'getEnglishLessons failed for user/{id} cause :::: {e}')
        time.sleep(0.5)
        
    
    try:
        print(f'getarabicLessons reqeust start user/{id}')
        getArabicLessons = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getArabicLessons request ,{getArabicLessons} in time = > {getArabicLessons.elapsed.total_seconds()}')
        counter.append(getArabicLessons.status_code)
        print(f'getarabicLessons reqeust done user/{id}')
        resaults[f'user/{id}-getArabicLessons'] = json.loads(getArabicLessons.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getArabicLessons'] = f'{e}'
        print(f'getarabicLessons failed for user/{id} cause :::: {e}')   
        time.sleep(0.5) 
    
    
    try:
        print(f'getSublessons start for user/{id}')
        for i in getpersianlessons.json()['data']:
            time.sleep(1)
            for j in i['sublessons']:
                subid = j['_id']
                
                print(f'get persiansublesson with id{subid} for user/{id}')
                getPersianSubLesson = requests.get(f'url' , headers={'Authorization': f'Bearer {token}'})
                a.append(f'user/{id} => getPersianSubLesson request ,{getPersianSubLesson} in time = > {getPersianSubLesson.elapsed.total_seconds()}')
                counter.append(getPersianSubLesson.status_code)
                resaults[f'user/{id}-getPersianSubLesson'] =json.loads(getPersianSubLesson.text)
                time.sleep(0.5)
                
                print(f'get englishsublesson with id{subid} for user/{id}')
                getEnglishSubLesson = requests.get(f'url' , headers={'Authorization': f'Bearer {token}'})
                a.append(f'user/{id} => getEnglishSubLesson request ,{getEnglishSubLesson} in time = > {getEnglishSubLesson.elapsed.total_seconds()}')
                counter.append(getEnglishSubLesson.status_code)
                resaults[f'user/{id}-getEnglishSubLesson'] = json.loads(getEnglishSubLesson.text)
                time.sleep(0.5)
                
                print(f'get arabicsublesson with id{subid} for user/{id}')
                getarabicSubLesson = requests.get(f'url' , headers={'Authorization': f'Bearer {token}'})
                a.append(f'user/{id} => getarabicSubLesson request ,{getarabicSubLesson} in time = > {getarabicSubLesson.elapsed.total_seconds()}')
                counter.append(getarabicSubLesson.status_code)
                resaults[f'user/{id}-getarabicSubLesson'] = json.loads(getarabicSubLesson.text)
                time.sleep(0.5)
                
        print(f'getSublessons done for user/{id}')
    except Exception as e:
        print(f'getSublessons failed for user/{id} cause :::: {e}')
        time.sleep(0.5)   
    
    
    try:
        print(f'getLevels start for user/{id}')
        getLevels = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getLevels request ,{getLevels} in time = > {getLevels.elapsed.total_seconds()}')
        counter.append(getLevels.status_code)
        print(f'getLevels done for user/{id}')
        resaults[f'user/{id}-getLevels'] = json.loads(getLevels.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getLevels'] = f'{e}'
        print(f'getLevels failed for user/{id} cause :::: {e}') 
        time.sleep(0.5)   
    
    
    try:
        print(f'getContents start for user/{id}')
        getContents = requests.get('url' , headers={'Authorization': f'Bearer {token}'})
        a.append(f'user/{id} => getContents request ,{getContents} in time = > {getContents.elapsed.total_seconds()}')
        counter.append(getContents.status_code)
        print(f'getContents done for user/{id}')
        resaults[f'user/{id}-getContents'] = json.loads(getContents.text)
        time.sleep(0.5)
    except Exception as e:
        resaults[f'user/{id}-getContents'] = f'{e}'
        print(f'getContents failed for user/{id} cause :::: {e}')    
        time.sleep(0.5)
    
    
    for l in getContents.json()['data']:
        contentId = l["_id"]
        time.sleep(1)
        try:
            print(f'seenContent start for user/{id}')
            seenContents = requests.put(f'url' , headers={'Authorization': f'Bearer {token}'})
            a.append(f'user/{id} => seenContents request ,{seenContents} in time = > {seenContents.elapsed.total_seconds()}')
            counter.append(seenContents.status_code)
            print(f'seenContent done for user/{id} and content/{contentId}')
            resaults[f'user/{id}-seenContents content/{contentId}'] = json.loads(seenContents.text)
            time.sleep(0.5)
        except Exception as e:
            resaults[f'user/{id}-seenContents content/{contentId}'] = f'{e}'
            print(f'seenContents failed for user/{id} and content/{contentId} cause :::: {e}')
            time.sleep(0.5)
    
    


threads = []
for i in range(700):    
    t = threading.Thread(target=print_name, args=(i,))
    t.start()
    threads.append(t)
    
    

for j in threads:
    j.join()

stop = timeit.default_timer()

count = 0
for i in a:
    print(i)
    
# serialized_data = json.loads(resaults)
json_object = json.dumps(resaults)

with open("resaut700Users.json" , "w") as f:
    f.write(json_object)


    
print('==============================================================================')
print('==============================================================================')
print('==============================================================================')

print(f'test run for {len(users)} virtual users successfull in time :: {stop-start}')
print(f'{len(resaults.keys())} try for request happened . . .')
print(f'{len(a)} requests done!')

print('==============================================================================')
print('==============================================================================')
print('==============================================================================')

success = [x for x in counter if x == 200]
internalError = [x for x in counter if x >= 500]
forbidden = [x for x in counter if x == 403]
unAuthorize = [x for x in counter if x == 401]
badRequest = [x for x in counter if x == 400]
print(f'{len(success)} requests 200 status code . . .')
print(f'{len(internalError)} requests 500 status code internal Error . . .')
print(f'{len(forbidden)} requests 403 status code internal Error . . .')
print(f'{len(unAuthorize)} requests 401 status code internal Error . . .')
print(f'{len(badRequest)} requests 400 status code internal Error . . .')

print('==============================================================================')
print('==============================================================================')
print('==============================================================================')
