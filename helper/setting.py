# cookie
""" 这里填cookie """
myCookie = "_uuid=E2D633B1-C9CC-E37E-6289-3A310D490ED571360infoc; buvid3=8170B38B-AB3D-4D9A-A05F-7A78B2103235167640infoc; fingerprint=05566bff21187560a35e6276c44d9ab7; buvid_fp=8170B38B-AB3D-4D9A-A05F-7A78B2103235167640infoc; buvid_fp_plain=8170B38B-AB3D-4D9A-A05F-7A78B2103235167640infoc; SESSDATA=3163a32c%2C1651034904%2C22bfe%2Aa1; bili_jct=ba87496978ec6cd9a7717d5f7e046eba; DedeUserID=430521080; DedeUserID__ckMd5=ed1a50c814af9670; sid=5ym7ohg9; bp_t_offset_430521080=586876722310080632"

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
