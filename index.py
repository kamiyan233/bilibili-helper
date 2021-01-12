import requests,json
from log import Log
from api import coinTodayExp,usernav,mangaSign,attentionVideo,popularVideo,liveSign,coinAdd,videoProgress,videoShare
from setting import bili_jct,coinnum,select_like,headers,SCKEY

# 日志
logger = Log()
# 通知到微信
def sendmsgtowx(text='服务器挂掉啦~~',desp=''):
    if SCKEY == '':
        logger.info('未配置推送微信')
        return
    else:
        url = "https://sc.ftqq.com/"+SCKEY+".send?text="+text+"&desp="+desp
        requests.get(url=url)
# 每日获取经验
class Exp:
    def __init__(self):
        # hasShare = 0
        self.getUserinfo()
        self.liveSign()
        self.mangaSign()
        self.getAttentionVideo()
        self.getPopularVideo()
        self.share(self.attention_aidList[1]['aid'])
        self.report(self.attention_aidList[1]['aid'],self.attention_aidList[1]['cid'],1000)
        # 投币(关注up主新视频和热门视频)
        if self.money < 1:
            logger.info('硬币不足，终止投币')
            return
        for item in self.attention_aidList + self.popular_aidList:
            exp = self.getCoinTodayExp()
            if exp == 50:
                logger.info('今日投币经验已达成')
                sendmsgtowx("今日经验已达成")
                return
            self.coin(item['aid'])
    # 获取用户信息
    def getUserinfo(self):
        try:
            res = requests.get(url=usernav,headers=headers)
            user_res = json.loads(res.text)['data']
            # print(user_res.text)
            money = user_res['money']
            uname = user_res['uname']
            self.uid = user_res['wallet']['mid']
            level_info = user_res['level_info']
            self.money = money
            logger.info('用户昵称：' + uname)
            logger.info('硬币余额：' + str(money))
            logger.info('当前等级：{},当前经验：{},下一级所需经验：{}'.format(level_info['current_level'],level_info['current_exp'],level_info['next_exp']-level_info['current_exp']))
        except:
            sendmsgtowx()
            logger.info('请求异常')
    # 获取关注的up最新发布的视频
    def getAttentionVideo(self):
        url = attentionVideo+'?uid='+str(self.uid)+'&type_list=8&from=&platform=web'
        res = requests.get(url=url,headers=headers)
        video_list = []
        for item in json.loads(res.text)['data']['cards']:
            video_list.append({'aid':json.loads(item['card'])['aid'],'cid':json.loads(item['card'])['cid']})
        self.attention_aidList = video_list
    def getCoinTodayExp(self):
        url = coinTodayExp
        res = requests.get(url=url,headers=headers)
        exp = json.loads(res.text)['data']
        # self.todayExp = exp
        return exp
    # 获取近期热门视频列表
    def getPopularVideo(self):
        url = popularVideo
        res = requests.get(url=url,headers=headers)
        video_list = []
        for item in json.loads(res.text)['data']['list']:
            video_list.append({'aid':item['aid'],'cid':item['cid']})
        self.popular_aidList = video_list
    # B站直播签到
    def liveSign(self):
        try:
            url = liveSign
            res = requests.get(url=url,headers=headers)
            logger.info('直播签到信息：'+json.loads(res.text)['message'])
        except:
            logger.info('请求异常')
    #  通过aid为视频投币
    def coin(self,aid):
        url = coinAdd
        post_data = {
            "aid": aid,
            "multiply": coinnum,
            "select_like": select_like,
            "cross_domain": "true",
            "csrf": bili_jct
        }
        res = requests.post(url=url,headers=headers,data=post_data)
        coinRes = json.loads(res.text)
        if coinRes['code'] == 0:
            # 投币成功
            logger.info('投币成功')
            self.getCoinTodayExp()
        else:
            logger.info('投币失败:' + coinRes['message'])
    # 上报视频进度
    def report(self, aid, cid, progres):
        url = videoProgress
        post_data = {
            "aid": aid,
            "cid": cid,
            "progres": progres,
            "csrf": bili_jct
            }
        res = requests.post(url=url, data=post_data,headers=headers)
        Res = json.loads(res.text)
        if Res['code'] == 0:
            # 投币成功
            logger.info('上报视频进度成功')
            self.getCoinTodayExp()
        else:
            logger.info('上报视频进度失败：' + Res['message'])
    #分享指定av号视频
    def share(self, aid):
        url = videoShare
        post_data = {
            "aid": aid,
            "csrf": bili_jct
            }
        res = requests.post(url=url, data=post_data,headers=headers)
        share_res = json.loads(res.text)
        if share_res['code'] == 0:
            self.hasShare = 1
            logger.info('视频分享成功')
        else:
            logger.info(share_res['message'])
    #漫画签到
    def mangaSign(self):
        try:
            url = mangaSign
            post_data = {
                "platform": 'android'
            }
            res = requests.post(url=url,headers=headers,data=post_data)
            if json.loads(res.text)['code'] == 0:
                logger.info('漫画签到成功')
            else:
                logger.info('漫画已签到或签到失败')
        except:
            logger.info('漫画签到异常')
Exp()