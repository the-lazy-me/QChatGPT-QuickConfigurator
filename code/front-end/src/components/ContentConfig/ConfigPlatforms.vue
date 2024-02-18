<template>
    <div>
        <div class="config-container">
            <div class="config-item">
                <h3>接入mirai</h3>
                <div class="switch-container">
                    <el-switch v-model="configPlatforms.mirai.enable" active-color="#13ce66" inactive-color="#ff4949"
                        active-text="开" inactive-text="关"></el-switch>
                </div>
                <el-form label-width="120px" label-position="left">
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>主机</span>
                            <el-tooltip class="item" effect="dark" content="Mirai主机地址，一般不动" placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.mirai.host" placeholder="127.0.0.1"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>端口</span>
                            <el-tooltip class="item" effect="dark" content="Mirai端口，默认8080，与mirai-api-http里面设置的保持一致"
                                placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.mirai.port" placeholder="8080"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>verifyKey</span>
                            <el-tooltip class="item" effect="dark" content="Mirai验证密钥，默认yirimirai，与mirai-api-http里面设置的保持一致"
                                placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.mirai.verifyKey" placeholder="yirimirai"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>QQ</span>
                            <el-tooltip class="item" effect="dark" content="Mirai QQ" placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.mirai.qq" placeholder="Mirai QQ"></el-input>
                    </el-form-item>

                </el-form>
            </div>
            <div class="config-item">
                <h3>接入go-cqhttp</h3>
                <div class="switch-container">

                    <el-switch v-model="configPlatforms.nakuru.enable" active-color="#13ce66" inactive-color="#ff4949"
                        active-text="开" inactive-text="关"></el-switch>
                </div>
                <el-form label-width="120px" label-position="left">
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>主机</span>
                            <el-tooltip class="item" effect="dark" content="gocq配置的主机地址，一般不动" placement="top"
                                trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.nakuru.host" placeholder="127.0.0.1"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>ws端口</span>
                            <el-tooltip class="item" effect="dark" content="gocq配置的WebSocket端口，与go-cqhttp的config.yml里面的保持一致"
                                placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.nakuru.ws_port" placeholder="8080"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>HTTP端口</span>
                            <el-tooltip class="item" effect="dark" content="gocq配置的HTTP端口" placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.nakuru.http_port" placeholder="gocq配置的HTTP端口"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>Token</span>
                            <el-tooltip class="item" effect="dark" content="gocq配置验证密钥，与go-cqhttp的config.yml里面的保持一致"
                                placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.nakuru.token" placeholder="gocq配置的验证密钥"></el-input>
                    </el-form-item>
                </el-form>
            </div>
            <div class="config-item">
                <h3>接入shamrock等onebot协议实现的机器人框架</h3>
                <div class="switch-container">

                    <el-switch v-model="configPlatforms.aiocqhttp.enable" active-color="#13ce66" inactive-color="#ff4949"
                        active-text="开" inactive-text="关"></el-switch>
                </div>
                <el-form label-width="120px" label-position="left">
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>主机</span>
                            <el-tooltip class="item" effect="dark" content="aiocqhttp主机地址，一般不动" placement="top"
                                trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.aiocqhttp.host" placeholder="127.0.0.1"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>端口</span>
                            <el-tooltip class="item" effect="dark" content="aiocqhttp端口，默认8080，与对应框架里面设置的保持一致"
                                placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.aiocqhttp.port" placeholder="8080"></el-input>
                    </el-form-item>
                </el-form>
            </div>
            <div class="config-item">
                <h3>接入QQ官方机器人</h3>
                <div class="switch-container">

                    <el-switch v-model="configPlatforms.qqBotpy.enable" active-color="#13ce66" inactive-color="#ff4949"
                        active-text="开" inactive-text="关"></el-switch>
                </div>
                <el-form label-width="120px" label-position="left">
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>AppId</span>
                            <el-tooltip class="item" effect="dark" content="QQ官方机器人的appid" placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.qqBotpy.appid" placeholder="QQ官方机器人的appid"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>Secret</span>
                            <el-tooltip class="item" effect="dark" content="QQ官方机器人的secret" placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-input v-model="configPlatforms.qqBotpy.secret" placeholder="QQ官方机器人的secret"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <div slot="label" class="label-custom">
                            <span>Intents</span>
                            <el-tooltip class="item" effect="dark"
                                content="控制监听的事件类型，public_guild_messages 频道消息；direct_message 频道私聊消息 public_messages Q群消息（需要权限）"
                                placement="top" trigger="hover">
                                <i class="el-icon-question"></i>
                            </el-tooltip>
                        </div>
                        <el-select v-model="configPlatforms.qqBotpy.intents" placeholder="请选择要接收的消息类型" multiple>
                            <el-option label="public_guild_messages" value="public_guild_messages" />
                            <el-option label="direct_message" value="direct_message" />
                            <el-option label="public_messages" value="public_messages" />
                        </el-select>
                    </el-form-item>
                </el-form>
                <p>注：public_guild_messages 频道消息；<br>direct_message 频道私聊消息<br> public_messages Q群消息（需要权限）</p>
            </div>

        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: "ConfigPlatforms",

    mounted() {
        axios.get('http://localhost:5000/read_platform_data')
            .then(response => {
                const configDetails = response.data['platform-adapters'];
                this.configPlatforms.mirai = configDetails[0];
                this.configPlatforms.nakuru = configDetails[1];
                this.configPlatforms.aiocqhttp = configDetails[2];
                this.configPlatforms.qqBotpy = configDetails[3];

            })
            .catch(error => {
                console.log(error);
            });
    },

    data() {
        return {
            configPlatforms: {
                mirai: {
                    enable: false,
                    host: '127.0.0.1',
                    port: 8080,
                    verifyKey: 'yirimirai',
                    qq: ''
                },
                nakuru: {
                    enable: false,
                    host: '127.0.0.1',
                    ws_port: 8080,
                    http_port: 5700,
                    token: ''
                },
                aiocqhttp: {
                    enable: false,
                    host: '127.0.0.1',
                    port: 8080
                },
                qqBotpy: {
                    enable: false,
                    appid: '',
                    secret: '',
                    intents: ['public_guild_messages', 'direct_message']
                }
            }
        };
    },
};
</script>
  
<style lang="css" scoped>
.config-container {
    width: 1000px;
    margin: 0 auto;
    padding: 20px 100px 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.config-item {
    width: 400px;
    margin: 20px 0;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
}

.config-item p {
    font-size: 14px;
    color: #666;
    margin-top: 10px;
    text-align: left;
}

.switch-container {
    margin-top: 10px;
    display: flex;
    justify-content: flex-start;
}

.el-form {
    margin-top: 20px;
}

.label-custom {
    font-size: 16px;

}

.label-custom i {
    margin-left: 10px;
    color: #13ce66;
    cursor: pointer;
}

div>>>.el-input__inner {
    font-size: 1.2em;
}

.el-select {
    width: 100%;
}
</style>
  