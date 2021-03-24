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
Tracker = []
Qty = []
Policy = []
Service = []
Price = []
ComparePrice = []
Shipping = []
Taxable = []
Image = []
CostPerItem = []
ImageSrc = []
ImagePosition = []
Status = []
Barcode = []
Card = []
SeoTitle = []
SeoDesc = []
ImgAltText = []


def read_mongoDB():
    client = pymongo.MongoClient('mongodb://116.62.11.8:27011')
    db = client.get_database("erpdb")
    db.authenticate('erpadmin', 'erpadmin112233')
    db = client["erpdb"]
    table = db["online"]
    result = []
    for item in table.find().limit(1):
        result.append(item)

    return result


def parse_data(data):
    for item in data:
        _handle = item.get('Product').get('ItemId')

        _title = item.get('Product').get('Attributes').get('name')

        _body = item.get('Product').get('Attributes').get('description')

        _published = 'TRUE'

        _name = item.get('Product').get('Attributes').get('brand')

        _type = item.get('Product').get('Attributes').get('name')

        sku = item.get('Product').get('Skus').get('Sku')
        print(len(sku))
        for index, i in enumerate(sku):
            Handle.append(_handle)
            Tracker.append('来赞宝')
            Qty.append(i.get('quantity'))
            Policy.append('continue')
            Service.append('manual')
            Price.append(i.get('price'))
            ComparePrice.append('')
            Shipping.append('TRUE')
            Taxable.append('TRUE')
            Image.append(i.get('Images').get('Image')[0])
            CostPerItem.append('')
            Status.append(i.get('Status'))
            Barcode.append('')
            Card.append('')
            SeoTitle.append('')
            SeoDesc.append('')
            Tags.append('')
            ImgAltText.append('')

            # 除了Handle字段，其他字段每个商品只出现一次
            if index == 0:
                Title.append(_title)
                Body.append(_body)
                Published.append(_published)
                Vendor.append(_name)
                Type.append(_type)

            else:
                Title.append('')
                Body.append('')
                Published.append('')
                Vendor.append('')
                Type.append('')

            if ('color_family' in i.keys()):
                Option1Name.append('color')
                Option1Value.append(i.get('color_family'))

            if ('size' in i.keys()):
                Option2Name.append('size')
                Option2Value.append(i.get('size'))

            if ('package_weight' in i.keys()):
                Grams.append(i.get('package_weight') * 1000)


def save_excel():
    data_df["Handle"] = Handle
    data_df["Title"] = Title
    data_df["Body (HTML)"] = Body
    data_df["Vendor"] = Vendor
    data_df["Type"] = Type
    data_df["Tags"] = Tags
    data_df["Published"] = Published
    data_df["Option1 Name"] = Option1Name
    data_df["Option1 Value"] = Option1Value
    data_df["Option2 Name"] = Option2Name
    data_df["Option2 Value"] = Option2Value
    # data_df["Option3 Name"] = Option3Name
    # data_df["Option3 Value"] = Option3Value
    data_df["Variant Grams"] = Grams
    data_df["Variant Inventory Tracker"] = Tracker
    data_df["Variant Inventory Qty"] = Qty
    data_df["Variant Inventory Policy"] = Policy
    data_df["Variant Fulfillment Service"] = Service
    data_df["Variant Price"] = Price
    data_df["Variant Compare at Price"] = ComparePrice
    data_df["Variant Requires Shipping"] = Shipping
    data_df["Variant Taxable"] = Taxable
    data_df["Variant Image"] = Image
    data_df["Cost per item"] = CostPerItem
    data_df["Status"] = Status
    data_df["Variant Barcode"] = Barcode
    data_df["Gift Card"] = Card
    data_df["SEO Title"] = SeoTitle
    data_df["SEO Description"] = SeoDesc
    data_df["Image Alt Text"] = ImgAltText
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
