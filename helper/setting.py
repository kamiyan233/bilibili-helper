# cookie
""" 这里填cookie """
myCookie = "buvid3=601C5578-9E07-4D88-81B3-0CC7E8E61CD0138390infoc; fingerprint3=6d31b15acac0e062d5296480c01946f6; fingerprint=619a3c29a34c56d408876b49ac53d60b; fingerprint_s=80e63cafb69b5496f26f98b13b8b521f; buvid_fp=601C5578-9E07-4D88-81B3-0CC7E8E61CD0138390infoc; buvid_fp_plain=601C5578-9E07-4D88-81B3-0CC7E8E61CD0138390infoc; PVID=1; innersign=0; bsource=search_baidu; _uuid=694173AA-A5C2-36D5-D72B-BCD0F95E676407375infoc; sid=ilnq2fiw; SESSDATA=c1b250f7%2C1650420339%2Ccb359%2Aa1; bili_jct=75826d509385722941338d2e2e338316; DedeUserID=1458508569; DedeUserID__ckMd5=21700d2ceeadfada"

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