<template>
    <div class="config-container">
        <!-- "openai-config": {
        "api-keys": [
            "sk-dn7bFSLvgFfFs1bJEf00F3D63c174d7a9301Ac5b8f89B21f"
        ],
        "base_url": "https://ai.lazyshare.top/v1",
        "chat-completions-params": {
            "model": "gpt-3.5-turbo-16k"
        },
        "request-timeout": 120
    }, -->
        <div class="config-item">
            <el-form :model="configAI" label-width="160px" label-position="left">
                <el-form-item label="API Key">
                    <div slot="label" class="label-custom">
                        <span>API Key</span>
                        <el-tooltip class="item" effect="dark" content="OpenAI 的API Key" placement="top" trigger="hover">
                            <i class="el-icon-question"></i>
                        </el-tooltip>
                    </div>
                    <el-form class="config-apikey">
                        <el-form-item v-for="(api, index) in configAI.apiKeys" :key="index">
                            <el-input v-model="configAI.apiKeys[index]" placeholder="请输入API Key"></el-input>
                            <el-button @click="configAI.apiKeys.splice(index, 1)" v-show="configAI.apiKeys.length > 1"
                                type="danger" icon="el-icon-delete" circle></el-button>
                            <el-button @click="configAI.apiKeys.push('')" v-show="configAI.apiKeys[index]" type="primary"
                                icon="el-icon-plus" circle></el-button>
                        </el-form-item>
                    </el-form>
                </el-form-item>
                <el-form-item label="Base URL">
                    <div slot="label" class="label-custom">
                        <span>Base URL</span>
                        <el-tooltip class="item" effect="dark" content="设置接口地址，后面一定要加/v1" placement="top" trigger="hover">
                            <i class="el-icon-question"></i>
                        </el-tooltip>
                    </div>
                    <el-input v-model="configAI.baseUrl" placeholder="请输入Base URL"></el-input>
                </el-form-item>
                <el-form-item label="Model">
                    <div slot="label" class="label-custom">
                        <span>Model</span>
                        <el-tooltip class="item" effect="dark" content="OpenAI 的Model" placement="top" trigger="hover">
                            <i class="el-icon-question"></i>
                        </el-tooltip>
                    </div>
                    <el-select v-model="configAI.model" placeholder="请选择Model">
                        <el-option label="gpt-3.5-turbo" value="gpt-3.5-turbo"></el-option>
                        <el-option label="gpt-3.5-turbo-16k" value="gpt-3.5-turbo-16k"></el-option>
                        <el-option label="gpt-4-vision-preview" value="gpt-4-vision-preview"></el-option>
                        <el-option label="gpt-4" value="gpt-4"></el-option>
                        <el-option label="gpt-4-32k" value="gpt-4-32k"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="Request Timeout">
                    <div slot="label" class="label-custom">
                        <span>Request Timeout</span>
                        <el-tooltip class="item" effect="dark" content="设置请求超时时间，以秒(s)为单位，对于耗时较长的模型，建议设置较大值" placement="top"
                            trigger="hover">
                            <i class="el-icon-question"></i>
                        </el-tooltip>
                    </div>
                    <el-input-number v-model="configAI.requestTimeout"  :min="120" :max="9999" placeholder="请输入超时时间，单位为秒"></el-input-number>
                </el-form-item>

            </el-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'ConfigAI',

    data() {
        return {
            configAI: {
                apiKeys: [''],
                baseUrl: '',
                model: '',
                requestTimeout: 0
            }
        };

    },

    mounted() {
        axios.get('http://localhost:5000/read_provider_data')
            .then(res => {
                console.log(res);
                this.configAI.apiKeys = res.data['openai-config']['api-keys'];
                this.configAI.baseUrl = res.data['openai-config']['base_url'];
                this.configAI.model = res.data['openai-config']['chat-completions-params']['model'];
                this.configAI.requestTimeout = res.data['openai-config']['request-timeout'];
            })
            .catch(err => {
                console.log(err);
            });

    },
};
</script>

<style lang="css" scoped>
.config-container {
    margin-top: 20px;

}

.config-item {
    margin: 0 auto;
    margin-top: 20px;
    padding: 20px;
    width: 800px;
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

.config-apikey {
    margin-top: 0;
}

.config-apikey .el-form-item:not(:last-child) {
    margin-bottom: 20px;
}

div>>>.el-input__inner {
    font-size: 1.2em;
}


.config-apikey div>>>.el-form-item__content {
    display: flex;
    width: 100%;
}

.el-select {
    width: 100%;
}

.el-input-number {
    width: 100%;
}

.el-button {
    margin-left: 20px;
}
</style>