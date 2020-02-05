from requests import get
from re import match
from requests.exceptions import Timeout
from multiprocessing import Pool
from gc import collect

global api, holders, chara, Name
api = 'https://tinygrail.com/api/'
null = 'nothing'
true = 'true'
false = 'false'
def get_text(url):
    return eval(get(url, timeout = 3).text)

def try_until(input_, error_ = ValueError, if_num = True):
    print(f"{input_}", end='')
    while True:
        try:
            output_ = int(input("")) if if_num == True else str(input(""))
            if output_ > 0:
                break
            else:
                print(f"格式错误，请重新{input_}", end='')
        except error_:
            print(f"格式错误，请重新{input_}", end='')
    return output_
chara_ = try_until("输入你要监测的角色id：")
chara = int(str(chara_))
try:
    Name = get_text(f'{api}chara/{chara}/')['Value']['Name']
except KeyError:
    raise Exception("角色id错误", "可能是角色没上市或者有其他原因")

print(f"你要监测的角色是：{Name}。按确认键继续", end = "")
input()

# 获取股东名单
holders_info = get_text(f'{api}chara/users/{chara}/1/1000')['Value']['Items']
holders = [i['Name'] for i in holders_info]

# 移除英灵殿
try:
    holders.remove('valhalla@tinygrail.com')
except ValueError:
    pass


whitelist = []
temp = ''
print("\n现在，你需要依次输入一列无需监测的用户白名单")
print("\n>>完成后，输入 done 来结束<<\n")
while temp != 'done':
    print("输入一个你不想监测的用户的id：", end='')
    temp = input("")
    if match("[a-z0-9]", temp) and temp != "done":
        whitelist.append(str(temp))
    elif temp in ["tinygrail", "done"]:
        continue
    else:
        print("格式错误，请重新", end='')
    
for ii in whitelist:
    try:
        holders.remove(ii)
    except:
        continue

print(f"\n你的白名单：{', '.join(whitelist)}\n按确认键继续", end = "")
input()

sleeping = try_until("\n你希望脚本多久监测一次？输入秒数（推荐至少20秒）：")

# initialization finished
####################################

print("\n开始监测……")
from time import sleep

depth = get_text(f"{api}chara/depth/{chara}")['Value']['Bids']

def cash(uid):
    url = api + 'chara/user/assets/'+ uid
    result = get_text(url)['Value']
    return int(result['Balance'])
def check_cash(holders):
    if __name__ == '__main__':
        with Pool(4) as p:
            ss = p.map(cash, holders)
    return ss
def check_depth():
    return get_text(f"{api}chara/depth/{chara}")['Value']['Bids'][0]

before = check_depth()
cash_before = check_cash(holders)
sleep(sleeping)
while True:
    try:
        now = check_depth()
        cash_now = check_cash(holders)

        if (now['Price'] != before['Price']) | (now['Amount'] != before['Amount']):
            content = f"买一价格变动：{before['Price']}-->{now['Price']}\n"
            content += f"买一数量变动：{before['Amount']}-->{now['Amount']}\n"
            changes = [cash_before[i] - cash_now[i] for i in range(len(cash_now))]
            content += "以下用户现金有变动：\n"
            for i in range(len(changes)):
                if changes[i] != 0:
                    content += f"用户id：{holders[i]}，{cash_before[i]}cc-->{cash_now[i]}cc\n"
            print(f'\n脚本监测到变动：\n\n'+content)

        cash_before = cash_now.copy()
        before = now.copy()
        collect()
        sleep(sleeping)
    except Exception as e:
        error_ = e
        break

print(f"监测停止，原因：\n{error_}")