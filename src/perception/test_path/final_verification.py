import sys

print("=== 环境最终验证 ===\n")

# 1. 检查Python解释器路径
print("1. Python解释器路径：")
print(f"   {sys.executable}")
print("   ✅ 正确" if "venv" in sys.executable else "   ❌ 错误：未使用虚拟环境")

# 2. 检查核心库
print("\n2. 检查核心库导入：")
libs = ['cv2', 'numpy', 'PIL', 'pytesseract']
for lib in libs:
    try:
        if lib == 'cv2':
            imported = __import__('cv2')
            version = imported.__version__
        elif lib == 'numpy':
            imported = __import__('numpy')
            version = imported.__version__
        elif lib == 'PIL':
            imported = __import__('PIL')
            version = imported.__version__
        elif lib == 'pytesseract':
            imported = __import__('pytesseract')
            version = "成功导入"
        print(f"   {lib}: ✅ 成功 (版本: {version})")
    except ImportError as e:
        print(f"   {lib}: ❌ 失败 - {e}")

print("\n=== 验证完成 ===")
