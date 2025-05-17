import qrcode

# 数据，这里是一个URL
data = 'https://zhty.netlify.app/'

# 创建一个QRCode实例
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加数据到QRCode实例中
qr.add_data(data)
qr.make(fit=True)

# 创建一个PIL Image实例
img = qr.make_image(fill='black', back_color='white')

# 显示图像（在支持图形界面的环境中）
img.show()

# 保存图像到文件
img.save('qrcode.png')
