import sys
print(f"Python解释器路径：{sys.executable}")
print(f"Python版本：{sys.version}")

try:
    import cv2
    print(f"OpenCV路径：{cv2.__file__}")
    print("✅ cv2 导入成功！")
except ImportError as e:
    print(f"❌ cv2 导入失败：{e}")