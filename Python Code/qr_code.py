import texteditor
import qrcode

generate_image=qrcode.make("geeksforgekks")
generate_image.save('image1.png')