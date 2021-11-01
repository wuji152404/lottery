import qrcode, os
import xlrd


def generate_qrcode(data, path, name):
    qr = qrcode.QRCode(version=10, error_correction=qrcode.ERROR_CORRECT_H,
                       box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(path + name + '.png')


def find_path(file, picname="photo"):
    picname= '\\{}'.format(picname)
    path, name = os.path.split(os.path.abspath(file))
    if not os.path.exists(path + picname):
        os.mkdir(path + picname)
    return path, name

if __name__ == '__main__':
    # generate_qrcode('dsaf dsfa f')
    file = r"C:\Users\65606\Desktop\new251.xlsx"
    path = find_path(file)[0] + "\\photo\\"
    print(path)
    databook = xlrd.open_workbook(file)
    datasheet1 = databook.sheet_by_name('Sheet1')
    codelist = datasheet1.col_values(0)  # 获取第一列内容，作为码值
    namelist = datasheet1.col_values(1)  # 获取第二列内容，为取名
    for i in range(len(codelist)):
        code = os.path.split(codelist[i])[-1]
        generate_qrcode(codelist[i], path, '{:0>6d}'.format(int(namelist[i])) + "_" + code)
    # generate_qrcode(codelist[i],path,str(int(namelist[i]))+"_"+code)
