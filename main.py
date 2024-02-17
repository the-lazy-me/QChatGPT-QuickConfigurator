from flask import Flask, jsonify
from flask_cors import CORS
import json
from flask import request

app = Flask(__name__)
CORS(app)


@app.route('/read_platform_data', methods=['GET'])
def read_json():
    read_data = {}

    # 读取第一个JSON文件，platform
    with open('../data/config/platform.json', 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
    platform = data1['platform-adapters']
    read_data['platform-adapters'] = platform
    # print(platform)

    # 返回JSON数据
    return jsonify(read_data)


@app.route('/read_provider_data', methods=['GET'])
def read_provider_json():
    read_data = {}

    # 读取第二个JSON文件，provider
    with open('../data/config/provider.json', 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
    read_data['openai-config'] = data2['openai-config']
    # print(providers)

    # 返回JSON数据
    return jsonify(read_data)


@app.route('/write_json', methods=['POST'])
def write_json():
    receive_data = request.json
    # 读取platform.json文件
    with open('../data/config/platform.json', 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)
        platform_adapters_data = data1['platform-adapters']

    # 读取provider.json文件
    with open('../data/config/provider.json', 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
        openai_config_data = data2['openai-config']

    # 遍历字典
    for key in platform_adapters_data:
        if key['adapter'] == 'yiri-mirai':
            key['enable'] = receive_data['platform']['mirai']['enable']
            key['host'] = receive_data['platform']['mirai']['host']
            key['port'] = receive_data['platform']['mirai']['port']
            key['qq'] = receive_data['platform']['mirai']['qq']
            key['verifyKey'] = receive_data['platform']['mirai']['verifyKey']
        if key['adapter'] == 'nakuru':
            key['enable'] = receive_data['platform']['nakuru']['enable']
            key['host'] = receive_data['platform']['nakuru']['host']
            key['http_port'] = receive_data['platform']['nakuru']['http_port']
            key['token'] = receive_data['platform']['nakuru']['token']
            key['ws_port'] = receive_data['platform']['nakuru']['ws_port']
        if key['adapter'] == 'aiocqhttp':
            key['enable'] = receive_data['platform']['aiocqhttp']['enable']
            key['host'] = receive_data['platform']['aiocqhttp']['host']
            key['port'] = receive_data['platform']['aiocqhttp']['port']
        if key['adapter'] == 'qq-botpy':
            key['enable'] = receive_data['platform']['qqBotpy']['enable']

    # 修改openai_config_data
    openai_config_data['api-keys'] = receive_data['provider']['apiKeys']
    openai_config_data['base_url'] = receive_data['provider']['baseUrl']
    openai_config_data['chat-completions-params']['model'] = receive_data['provider']['model']
    openai_config_data['request-timeout'] = receive_data['provider']['requestTimeout']

    # 写入platform.json文件
    with open('../data/config/platform.json', 'w', encoding='utf-8') as file1:
        json.dump(data1, file1, ensure_ascii=False, indent=4)

    # 写入provider.json文件
    with open('../data/config/provider.json', 'w', encoding='utf-8') as file2:
        json.dump(data2, file2, ensure_ascii=False, indent=4)

    return jsonify(receive_data)


if __name__ == '__main__':
    app.run()
