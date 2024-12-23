'''
Author: mozzat taogroups@163.com
Date: 2024-12-07 22:51:20
LastEditors: mozzat taogroups@163.com
LastEditTime: 2024-12-23 10:07:38
FilePath: /pythonProject/util.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import re
# 通过产品名称获取重量
def getProductWeightByName(name): 
    if "-" in name.lower():
        pattern1 = r"(\d+-\d+g)"
        match1 = re.search(pattern1, name)
        if match1:
            extracted_text = match1.group(0)
            print(f"提取的文本: {extracted_text}")
            if "kg" in extracted_text.lower():
                extracted_text = extracted_text.replace("kg","")
                arr = extracted_text.split("-")
                extracted_text = str((float(arr[0])+float(arr[1]))/2) + "kg"
                return extracted_text
            elif "g" in extracted_text.lower():
                extracted_text = extracted_text.replace("g","")
                arr = extracted_text.split("-")
                extracted_text = str((float(arr[0])+float(arr[1]))/2) + "g"
                return extracted_text

    # 正则表达式模式
    pattern = r"(\d+\.?\d*)(g|G|KG|kg)"
    # 使用 re.search 查找匹配
    match = re.search(pattern, name)
    if match:
    # 提取匹配的数字和单位部分
        extracted_text = match.group(0)
        print(f"提取的文本: {extracted_text}")
        return extracted_text
    return ""  

# 通过产品名称获取质量
def getProductQualityByName(name):
    # 正则表达式模式
    pattern = r"(\d+\.?\d*)"
    # 使用 re.search 查找匹配
    match = re.search(pattern, name)
    if match:
    # 提取匹配的数字和单位部分
        extracted_text = match.group(0)
        print(f"提取的文本: {extracted_text}")
        return float(extracted_text)
    else:

        
        print("未找到匹配的文本")
    return 0.0  

# 判断是不是特卖产品 以T或者B开头
def jundgeIsLowPriceProduct(string):
    # return is_b_followed_by_chinese_or_dash(string)
    string = string.upper()
    isStart = string.startswith(("T", "B"))
    if isStart == True:
        return is_third_char_chinese(string)
    else:
        return False

def getResultWeight(w):
    weight = getProductWeightByName(w)
    weightNum = getProductQualityByName(weight)
    # 表示千克
    weightS = str(weight).lower()
    if weightS.find("g") != -1: 
        # 全部转成千克计算
        weightNum = weightNum / 1000.0
    return weightNum

def is_b_followed_by_chinese_or_dash(s):
    string = s.upper()
    pattern = r'^[BT][\u4e00-\u9fa5-]+$'
    return bool(re.match(pattern, string))



def is_third_char_chinese(s):
    # 检查字符串长度是否大于等于3
    if len(s) < 3:
        return False
    
    # 使用正则表达式匹配第三个字符是否为中文字符
    match = re.match(r'.{2}[\u4e00-\u9fa5-]', s)
    
    return match is not None



# isChina = jundgeIsLowPriceProduct("Tsss500g")
# isChina1 = jundgeIsLowPriceProduct("T美国极佳牛仔骨500")
# isChina2 = jundgeIsLowPriceProduct("T美国极佳牛仔骨")
# isChina3 = jundgeIsLowPriceProduct("T品-美国极佳牛仔骨")
# print(isChina,isChina1,isChina2,isChina3)