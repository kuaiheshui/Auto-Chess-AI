import cv2
import pytesseract
# from PIL import Image
import numpy as np
import os
from pathlib import Path  # 用于优雅处理路径

# 告诉Python Tesseract引擎在哪 
# 请根据实际安装路径修改下面的路径，注意保留开头的 r
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 1. 模拟：未来这里会替换为实时截屏，现在先用一张静态截图测试
# 请确保在 assets/screenshots/ 下有一张图片，命名为 test_ui.jpg
# --- 动态构建截图绝对路径---
# 获取当前脚本文件的目录
current_dir = Path(__file__).parent  # src/perception
# 向上回退两级到项目根目录 (Auto-Chess-AI)
project_root = current_dir.parent.parent
# 构建完整的截图路径
screenshot_path = project_root / "assets" / "screenshots" / "test_ui.jpg"
# 将Path对象转换为字符串（某些旧版OpenCV需要）
screenshot_path = str(screenshot_path)

print(f"正在尝试从以下位置读取截图：\n{screenshot_path}")

# 检查文件是否存在
if not os.path.exists(screenshot_path):
    print("错误：文件不存在！请检查：")
    print(f"1. 文件路径是否正确：{screenshot_path}")
    print("2. 文件是否被正确放置在 assets/screenshots/ 目录下")
    print("3. 文件名是否为 test_ui.jpg（注意大小写和扩展名）")
    exit()

# 图像读取和处理
image = cv2.imread(screenshot_path)
# screenshot_path = "../assets/screenshots/test_ui.jpg"

# image = cv2.imread(screenshot_path)

if image is None:
    print(f"错误：找不到截图文件，请检查路径: {screenshot_path}")
    exit()

# 2. 图像预处理示例：转换为灰度图（许多操作需要在灰度图上进行）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("图像加载与预处理完成。")

# 3. 尝试识别（假设数字在画面顶部中央区域）
# 你需要根据实际图像，调整下面的坐标 (x, y, width, height)
gold_region = (100, 50, 150, 60)  # 示例：(x, y, w, h)，请自行调整
x, y, w, h = gold_region
gold_image = gray[y:y+h, x:x+w]

# 对数字区域进行阈值处理，使其更清晰
_, thresh = cv2.threshold(gold_image, 150, 255, cv2.THRESH_BINARY_INV)

# 4. 使用pytesseract识别数字
# 配置Tesseract只识别数字
custom_config = r'--oem 3 --psm 13 -c tessedit_char_whitelist=0123456789'
gold_text = pytesseract.image_to_string(thresh, config=custom_config).strip()

print(f"识别出的数字为: {gold_text if gold_text else '未识别到数字'}")

# 5. （可选）显示处理过程中的图像，用于调试
cv2.imshow('Original Screenshot', image)
cv2.imshow('Gold Region (Thresholded)', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("基础流程测试完成！")
