import pymongo
import pandas as pd

data_df = pd.DataFrame()
Handle = []
Title = []
Body = []
Vendor = []
Type = []
Tags = []
Published = []
Option1Name = []
Option1Value = []
Option2Name = []
Option2Value = []
Option3Name = []
Option3Value = []
Grams = []
Qty = []
Price = []
ComparePrice = []
ImageSrc = []
ImagePosition = []


def read_mongoDB():
    client = pymongo.MongoClient('mongodb://116.62.11.8:27011')
    db = client.get_database("erpdb")
    db.authenticate('erpadmin', 'erpadmin112233')
    db = client["erpdb"]
    table = db["online"]
    result = []
    for item in table.find().limit(20):
        result.append(item)

    return result


def parse_data(data):
    for item in data:
        _handle = item.get('Product').get('ItemId')
        Handle.append(_handle)
        _title = item.get('Product').get('Attributes').get('name')
        Title.append(_title)
        _body = item.get('Product').get('Attributes').get('description')
        Body.append(_body)
        _published = 'TRUE'
        Published.append(_published)
        _name = item.get('Product').get('Attributes').get('brand')
        Vendor.append(_name)
        _type = item.get('Product').get('Attributes').get('name')
        Type.append(_type)
        _tag = item.get('Product').get('categoryNameDesc')
        Tags.append(_tag)


def save_excel():
    data_df["Handle"] = Handle
    data_df["Title"] = Title
    data_df["Body (HTML)"] = Body
    data_df["Vendor"] = Vendor
    data_df["Type"] = Type
    data_df["Tags"] = Tags
    data_df["Published"] = Published
    # data_df["Option1 Name"] = Option1Name
    # data_df["Option1 Value"] = Option1Value
    # data_df["Option2 Name"] = Option2Name
    # data_df["Option2 Value"] = Option2Value
    # data_df["Option3 Name"] = Option3Name
    # data_df["Option3 Value"] = Option3Value
    # data_df["Variant Grams"] = Grams
    # data_df["Variant Inventory Qty"] = Qty
    # data_df["Variant Price"] = Price
    # data_df["Variant Compare at Price"] = ComparePrice
    # data_df["Image Src"] = ImageSrc
    # data_df["Image Position"] = ImagePosition

    writer = pd.ExcelWriter('sku.xlsx')
    data_df.to_excel(writer, sheet_name='product_template', index=False)
    writer.save()


def main():
    data = read_mongoDB()

    parse_data(data)

    save_excel()


if __name__ == '__main__':
    main()
