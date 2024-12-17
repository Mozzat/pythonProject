import sqlite3
import openpyxl
# 创建数据库
def createDB():
    conn = sqlite3.connect('ProductListDb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 productCode TEXT NOT NULL,
                 productName TEXT NOT NULL,
                 productCategory TEXT NOT NULL,
                 productBasePrice TEXT NOT NULL,
                 productCK TEXT NOT NULL,
                 productUnit TEXT NOT NULL,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# 更新
def updateProductList(filePath):

    # 读取文件数据
    # exclePath = '/Users/mozzat/Desktop/pythonProject/分仓库存查询.xlsx'
    exclePath = filePath
    wb = openpyxl.load_workbook(exclePath)
    sheet = wb.active

    conn = sqlite3.connect('ProductListDb.db')
    c = conn.cursor()

    index = 0
    productCodeArr = []
    #  分组处理数据
    for row in sheet.iter_rows(min_row=1, values_only=True):
        if index == 0:
            index += 1
            continue
        if row[0] not in productCodeArr:
            productCodeArr.append(row[0])
        else:
            continue
        productCode = row[0]
        productName = row[1]
        productCategory = row[2]
        productBasePrice = row[4]
        productCK = row[7]
        productUnit = row[9]
        
        # 插入数据到数据库
        c.execute("INSERT OR IGNORE INTO products (productCode, productName, productCategory, productBasePrice, productCK, productUnit) VALUES (?, ?, ?, ?, ?, ?)",(productCode,productName,productCategory,productBasePrice,productCK,productUnit,))

    conn.commit()
    conn.close()

# 获取产品信息
def queryProductByProductCode(productCode):
    conn = sqlite3.connect('ProductListDb.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE productCode = ?", (productCode,))
    rows = c.fetchall()
    conn.close()
    return rows
# createDB()
# updateProductList("")
# product = queryProductByProductCode("0203F4N0001")
# print(product)