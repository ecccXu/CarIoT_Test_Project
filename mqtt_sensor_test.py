import paho.mqtt.client as mqtt
import time
import json

# 配置MQTT服务器（用国内的emqx）
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "vehicle/sensor/test"  # 和之前的主题保持一致


# --------------------------
# 订阅端回调函数（接收消息）
# --------------------------
def on_connect_sub(client, userdata, flags, rc):
    if rc == 0:
        print("订阅端已连接到MQTT服务器 ✅")
        client.subscribe(TOPIC)  # 连接成功后订阅主题
    else:
        print(f"订阅端连接失败，错误码: {rc} ❌")


def on_message_sub(client, userdata, msg):
    # 收到消息后打印
    print(f"\n收到传感器数据 📩:")
    print(f"主题: {msg.topic}")
    print(f"内容: {json.loads(msg.payload.decode('utf-8'))}")


# --------------------------
# 发布端（模拟传感器）
# --------------------------
def publish_sensor_data(publish_client):
    temperature = 25.0
    while True:
        # 模拟传感器数据
        sensor_data = {
            "device_id": "sensor_001",
            "temperature": round(temperature, 1),
            "humidity": 55,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # 发布消息
        result = publish_client.publish(
            topic=TOPIC,
            payload=json.dumps(sensor_data),
            qos=0
        )
        # 检查发布结果
        if result.rc == 0:
            print(f"\n已发布传感器数据 🚀: {sensor_data}")
        else:
            print(f"发布失败 ❌, 错误码: {result.rc}")

        temperature += 0.5
        time.sleep(3)  # 每3秒发一次


# --------------------------
# 主程序：启动订阅端+发布端
# --------------------------
if __name__ == "__main__":
    # 1. 初始化订阅端
    sub_client = mqtt.Client(client_id="sub_client_001")  # 客户端ID唯一
    sub_client.on_connect = on_connect_sub
    sub_client.on_message = on_message_sub
    sub_client.connect(BROKER, PORT, keepalive=60)  # keepalive设为60秒避免断连
    sub_client.loop_start()  # 启动订阅端的网络循环（后台运行）

    # 2. 初始化发布端
    pub_client = mqtt.Client(client_id="pub_client_001")  # 客户端ID和订阅端不同
    pub_client.connect(BROKER, PORT, keepalive=60)
    pub_client.loop_start()  # 启动发布端的网络循环

    # 3. 开始发布传感器数据
    try:
        publish_sensor_data(pub_client)
    except KeyboardInterrupt:
        print("\n程序终止，断开连接...")
        sub_client.loop_stop()
        pub_client.loop_stop()
        sub_client.disconnect()
        pub_client.disconnect()