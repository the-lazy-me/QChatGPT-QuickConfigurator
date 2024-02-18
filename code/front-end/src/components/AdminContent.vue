<template>
    <div>
        <div class="config-platforms">
            <h2>1. 登录框架配置</h2>
            <ConfigPlatforms ref="platformData" />
        </div>

        <div class="config-ai">
            <h2>2. AI聊天配置</h2>
            <ConfigAI ref="providerData"/>
        </div>
        <el-button type="primary" round @click="submitConfig">提交配置</el-button>
    </div>
</template>

<script>
import ConfigPlatforms from './ContentConfig/ConfigPlatforms.vue';
import ConfigAI from './ContentConfig/ConfigAI.vue';
import axios from 'axios';


export default {
    name: 'AdminContent',

    components: {
        ConfigPlatforms,
        ConfigAI
    },



    methods: {
        submitConfig() {
            this.$message({
                message: '配置提交成功',
                type: 'success'
            });
            const submitData = {
                platform: this.$refs.platformData.configPlatforms,
                provider: this.$refs.providerData.configAI
            };
            console.log(submitData);
            axios.post('http://localhost:5000/write_json', submitData)
                .then(res => {
                    console.log(res);
                })
                .catch(err => {
                    console.log(err);
                });

        }
    }
};
</script>

<style lang="css" scoped>
.config-platforms {
    margin-top: 50px;
    padding: 20px 0;
}

.config-ai {
    margin-top: 50px;
    padding: 20px 0;
}

.el-button {
    margin-top: 50px;
}
</style>