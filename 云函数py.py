import requests
# server酱开关，填0不开启(默认)，填2同时开启cookie失效通知和签到成功通知
sever = '2'
# 填写server酱sckey,不开启server酱则不用填（自己更改）
sckey = 'SCU123521T49ffe7a3ba2b59b9105ce3bec15b08355fa37707333b1'
# 填入glados账号对应cookie
cookie = 'koa:sess=eyJ1c2VySWQiOjU3NTMxLCJfZXhwaXJlIjoxNjMwNDY4NjkxMzg0LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=x1JInrlvQ6zVPvyShWc_OIoMmLE'
referer = 'https://glados.rocks/console/checkin'

def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados_network'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()
