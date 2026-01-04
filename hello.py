import os

# 创建项目目录结构
os.makedirs("CarTest_MQTT/UI/css", exist_ok=True)
os.makedirs("CarTest_MQTT/UI/pages", exist_ok=True)

# 创建空文件
files_to_create = [
    "UI/index.html",
    "UI/css/style.css",
    "UI/pages/dashboard.html",
    "UI/pages/sensor-config.html",
    "UI/pages/mqtt-config.html",
    "UI/pages/test-execution.html",
    "UI/pages/data-results.html",
    "UI/README.md"
]

for file_path in files_to_create:
    with open(file_path, 'w') as f:
        pass  # 创建空文件

print("项目结构创建完成！")
print("UI/")
print("├── index.html")
print("├── css/")
print("│   └── style.css")
print("├── pages/")
print("│   ├── dashboard.html")
print("│   ├── sensor-config.html")
print("│   ├── mqtt-config.html")
print("│   ├── test-execution.html")
print("│   └── data-results.html")
print("└── README.md")
