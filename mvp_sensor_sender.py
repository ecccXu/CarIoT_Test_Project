# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import time
import random

# --- 配置信息 ---
# 1. MQTT服务器地址 (使用公共免费服务器)
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883

# 2. 模拟设备ID和MQTT主题
DEVICE_ID = "mvp_test_device_001"
MQTT_TOPIC = f"car/sensor/{DEVICE_ID}/data"  # 定义一个规范的主题

# 3. 发送间隔（秒）
SEND_INTERVAL = 5


# --- 配置结束 ---

# 当客户端连接到MQTT服务器时的回调函数
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("成功连接到MQTT服务器")
    else:
        print(f"连接失败，错误代码: {rc}")


# 创建MQTT客户端实例
client = mqtt.Client(client_id=DEVICE_ID)
client.on_connect = on_connect

try:
    # 连接到MQTT服务器
    print(f"正在连接到 {MQTT_BROKER}:{MQTT_PORT}...")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # 启动一个后台线程来处理网络通信
    client.loop_start()

    print(f"开始模拟数据上报，主题: {MQTT_TOPIC}，间隔: {SEND_INTERVAL}秒")
    print("按 Ctrl+C 停止程序")

    while True:
        # 1. 模拟生成车载传感器数据 (温度范围: -10°C ~ 50°C)
        temperature = round(random.uniform(-10, 50), 2)
        humidity = round(random.uniform(30, 80), 2)

        # 2. 将数据组织成JSON格式
        payload = {
            "device_id": DEVICE_ID,
            "timestamp": int(time.time()),
            "temperature": temperature,
            "humidity": humidity
        }
        payload_str = json.dumps(payload)

        # 3. 发布消息到指定的MQTT主题 (QoS=1)
        client.publish(MQTT_TOPIC, payload_str, qos=1)
        print(f"已发送: {payload_str}")

        # 等待一段时间
        time.sleep(SEND_INTERVAL)

except KeyboardInterrupt:
    print("\n程序被用户中断")
except ConnectionRefusedError:
    print(f"连接失败，请检查MQTT服务器 {MQTT_BROKER}:{MQTT_PORT} 是否可访问")
finally:
    client.loop_stop()
    client.disconnect()
    print("已断开与MQTT服务器的连接")