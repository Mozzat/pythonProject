<!--
 * @Author: mozzat taogroups@163.com
 * @Date: 2024-12-07 22:13:34
 * @LastEditors: mozzat taogroups@163.com
 * @LastEditTime: 2024-12-12 17:37:17
 * @FilePath: /pythonProject/readme.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
### 思路
========== 前期准备 ===========
1.创建字段对应码表(用于字段解析)
2.创建产品码表(用于产品匹配) 

### 需求分析


### 临时需求整理
1 特卖不消耗原料 不参与分摊原料成本 T、B 开头

多品：
看是不是余料仓，如果是，原料的总成本为0，但实际领用量保持不变
1.总成本：重复的项目总成本相加，求和
2.实际领用量：总成本/物料出库价，求和
3.原料摊销KG=原料实际领用总量/（品的报工数*货品规格的合计）*品的报工数*规格，记得锁定
4.原料摊销金额=原料总成本/（品的报工数*货品规格）*品的报工数*规格，记得锁定
5.辅料摊销金额=辅料总成本/品的总报工数*单品的报工数，记得锁定
前后单位一致则不用换算
单片成本=（原料摊销金额+辅料摊销金额）/各单品的报工数
出品率=单品报工数*规格/原料摊销KG（记得换算）

单品：
单片成本=品的总成本/品的报工数
出品率=单品报工数*货品规格/（原料的）实际领用量 
  （注意，实际领用量只看“原料”）  
（“货品名称”后面没有重量的要去“(分仓库存查询”查，物料名称后面无重量的默认是一公斤，前后以1000g为标准换算，前后都要看）

当同任务单多个货品规格相同时可直接计算单片成本与出品率。（单片成本=品的总成本/品的总报工数，出品率=总报工数*货品规格/总实际领用量 ）


ps 临时代码
if item.lenth > 1:
            #  多品
            print('多品')



        else :
            #  单品
            item1 = item[0]
            for item in totalArr: 
                # 总成本
                length = len(item) -1
                amountTurbe = item[length]
                firstTurbe = item[0]
                weight = util.getProductWeightByName(firstTurbe[2])
                weightNum = util.getProductQualityByName(weight)
                for dic in item:
                    bgs = dic[4]
                    sjlql = dic[9]
                    if dic[6] == '原料':
                        # 判断千克和g
                        # totalWeight = bgs * weight
                        # 表示千克
                        weightS = str(weight).lower()
                        if weightS.find("g") != -1: 
                            totalWeight = bgs * weightNum / 1000
                        else:
                            totalWeight = bgs * weightNum

                        sjlqlS = str(sjlql).lower()
                        if sjlqlS.find("g") != -1:
                            sjlqlNum = util.getProductQualityByName(str(dic[9]))
                            sjlql = sjlqlNum / 1000
                        
                        cpl = totalWeight / sjlql
                        print("出品率", cpl,firstTurbe[1])
                    else:
                        continue