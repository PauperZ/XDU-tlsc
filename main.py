import os
import random
import time

from PIL import Image, ImageDraw, ImageFont

general = Image.open("./image/general.png")
ewg = Image.open("./image/ewg.png")
ewr = Image.open("./image/ewr.png")
nslg = Image.open("./image/nslg.png")
nslr = Image.open("./image/nslr.png")
nsrg = Image.open("./image/nsrg.png")
nsrr = Image.open("./image/nsrr.png")
nssg = Image.open("./image/nssg.png")
nssr = Image.open("./image/nssr.png")
font = "digital-7.ttf"
green = (0, 255, 78)
red = (255, 0, 0)

def creat_ewtime(nsstatus, ewtime):
    """生成旋转的东西红绿灯剩余时间图像"""
    width = 50
    height = 45
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font_type = ImageFont.truetype(font, 45)
    # 输出文字:
    if(nsstatus == 2):
        draw.text((0, 0), str(ewtime), font=font_type, fill=green)
    else:
        draw.text((0, 0), str(ewtime), font=font_type, fill=red)

    #旋转倒计时
    imaget = image.transpose(Image.Transpose.ROTATE_270)

    return imaget

def creat_frame(nsstatus, nstime, ewtime):
    """生成单帧红绿灯状态图像"""
    frame = Image.new('RGB', general.size, 'white')
    frame.paste(general, (0, 0))

    if(nsstatus == 0):
        #南北路口直行
        draw = ImageDraw.Draw(frame)
        nslr.thumbnail((50, 40))
        nssg.thumbnail((36, 45))
        nsrg.thumbnail((50, 40))
        frame.paste(nslr, (148, 161))
        frame.paste(nssg, (213, 159))
        frame.paste(nsrg, (324, 161))
        font_type = ImageFont.truetype(font, 45)
        draw.text((266, 166), str(nstime), font=font_type, fill=green)
        #东西路口红灯
        frame.paste(ewr, (618, 393))
        ewt = creat_ewtime(nsstatus, ewtime)
        frame.paste(ewt, (610, 448))

    if (nsstatus == 1):
        # 南北路口左转
        draw = ImageDraw.Draw(frame)
        nslg.thumbnail((50, 40))
        nssr.thumbnail((36, 45))
        nsrg.thumbnail((50, 40))
        frame.paste(nslg, (148, 161))
        frame.paste(nssr, (213, 159))
        frame.paste(nsrg, (324, 161))
        font_type = ImageFont.truetype(font, 45)
        draw.text((266, 166), str(nstime), font=font_type, fill=green)
        # 东西路口红灯
        frame.paste(ewr, (618, 393))
        ewt = creat_ewtime(nsstatus, ewtime)
        frame.paste(ewt, (610, 448))

    if (nsstatus == 2):
        # 南北路口红灯
        draw = ImageDraw.Draw(frame)
        nslr.thumbnail((50, 40))
        nssr.thumbnail((36, 45))
        nsrg.thumbnail((50, 40))
        frame.paste(nslr, (148, 161))
        frame.paste(nssr, (213, 159))
        frame.paste(nsrg, (324, 161))
        font_type = ImageFont.truetype(font, 45)
        draw.text((266, 166), str(nstime), font=font_type, fill=red)
        # 东西路口绿灯
        frame.paste(ewg, (618, 393))
        ewt = creat_ewtime(nsstatus, ewtime)
        frame.paste(ewt, (610, 448))

    return frame


def frame_to_gif(framelist, gif_name):
    """png合成gif图像"""
    # 以第一张图片作为开始，将后续139张图片合并成 gif 动态图
    # save_all 保存图像;transparency 设置透明背景色;duration 单位毫秒，动画持续时间，
    # loop=0 无限循环;disposal=2 恢复原背景颜色。
    framelist[0].save(gif_name, format='GIF', save_all=True, append_images=framelist[1:], transparency=100, duration=1000, loop=0, disposal=2)


if __name__ == '__main__':
    framelist = []
    for i in range(0, 140):
        if i < 20:
            frame = creat_frame(0, 20 - i, 60 - i)
            framelist.append(frame)
            frame.save("./png_results/{}.png".format(i))
        elif i < 60:
            frame = creat_frame(1, 60 - i, 60 - i)
            framelist.append(frame)
            frame.save("./png_results/{}.png".format(i))
        else:
            frame = creat_frame(2, 140 - i, 140 - i)
            framelist.append(frame)
            frame.save("./png_results/{}.png".format(i))


    frame_to_gif(framelist, "tlsc.gif")


