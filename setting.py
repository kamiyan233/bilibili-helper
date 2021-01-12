# cookie
""" 这里填cookie """
myCookie = ""

cookies = dict([l.split("=", 1) for l in myCookie.split("; ")])

# 3个用户相关参数
bili_jct = cookies['bili_jct']
SESSDATA = cookies['SESSDATA']
DedeUserID = cookies['DedeUserID']

# server酱
SCKEY = ""
# 每次投入硬币数量 1 或 2
coinnum = 1
# 投币时是否点赞
select_like = 0 # 0 不点赞 1 点赞


useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"

headers = { "Content-Type": "application/x-www-form-urlencoded",
        "Cookie":"bili_jct=" + bili_jct+ "; SESSDATA=" + SESSDATA + "; DedeUserID=" + DedeUserID,
        "Referer": "https://www.bilibili.com/",
        "User-Agent": useragent}