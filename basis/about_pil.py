# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
图片处理相关
'''

from PIL import Image, ImageDraw, ImageFont
import os


def create_text_and_pic_watermark(src, dest, wm_pic, wm_text="Xiao Yaoyao"):
    '''
    分别在图片的上中下三个位置加水印
    :param src:
    :param dest:
    :param wm_pic:
    :param wm_text:
    :return:
    '''
    image = Image.open(src)
    font_attr = ImageFont.truetype("data/ttf/South Bold Italic.ttf", 150)
    # font_attr = ImageFont.truetype("data/ttf/Piikoi Regular.ttf", 150)
    layer = image.convert("RGBA")
    layer = layer.transpose(Image.ROTATE_270)
    text_overlay = Image.new("RGBA", layer.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    text_size_x, text_size_y = image_draw.textsize(wm_text, font=font_attr)
    wm_fill = (255, 255, 255, 60)
    # 左上角
    text_lefttop = (10, 10)
    image_draw.text(text_lefttop, wm_text, font=font_attr, fill=wm_fill)
    # 中间
    test_center = ((layer.size[0] - text_size_x) / 2, (layer.size[1] - text_size_y) / 2)
    image_draw.text(test_center, wm_text, font=font_attr, fill=wm_fill)
    # 右下角
    text_rightbottom = (layer.size[0] - text_size_x - 10, layer.size[1] - text_size_y - 10)
    image_draw.text(text_rightbottom, wm_text, font=font_attr, fill=wm_fill)
    after = Image.alpha_composite(layer, text_overlay)

    water_image = Image.open(wm_pic)
    water_image = water_image.convert("RGBA")
    warter_image_x = water_image.size[0]
    warter_image_y = water_image.size[1]
    water_image = water_image.resize((int(warter_image_x /3), int(warter_image_y / 3)))
    # water_image = water_image.resize((int(warter_image_x / 10), int(warter_image_y / 10)))
    # 透明度
    water_image_mask = water_image.convert("L").point(lambda x: min(x, 80))
    water_image.putalpha(water_image_mask)
    warter_image_x, warter_image_y = water_image.size
    # 右上角
    # after.paste(water_image, (layer.size[0] - watermark_x, 0), water_image)
    # 左下角
    after.paste(water_image, (10, layer.size[1] - warter_image_y - 10), water_image)
    # after.show()
    after.save(dest)


def add_wartermark_all_image(src, dest, wm_pic, wm_text):
    '''
    给文件夹所有图片加水印
    :param src: 原图片文件夹
    :param dest: 加水印后图片文件夹
    :param wm_pic: 水印图片
    :param wm_text: 水印文本
    :return:
    '''
    pics = os.listdir(src)
    for pic in pics:
        if pic.startswith("."):
            continue
        file_name = pic[0: pic.find(".")]
        dest_name = f"{file_name}_wm.png"
        dest_file = f"{dest}/{dest_name}"
        src_file = f"{src}/{pic}"
        create_text_and_pic_watermark(src_file, dest_file, wm_pic, wm_text=wm_text)
        print(f"Add WaterMark {pic} => {dest_name}")


if __name__ == '__main__':
    # src = "/Users/wangqiang/MyDocuments/yicheng/origin0524/01.jpeg"
    # dest = "/Users/wangqiang/MyDocuments/yicheng/watermark0524/01_wm.png"
    # wm_pic = "data/pics/djs02.png"
    # create_text_and_pic_watermark(src, dest, wm_pic, wm_text="YanHongGuan@douban")

    src = "/Users/wangqiang/MyDocuments/yicheng/origin0530"
    dest = "/Users/wangqiang/MyDocuments/yicheng/watermark0530"
    wm_pic = "data/pics/djs02.png"
    add_wartermark_all_image(src, dest, wm_pic, wm_text="YanHongGuan@douban")
