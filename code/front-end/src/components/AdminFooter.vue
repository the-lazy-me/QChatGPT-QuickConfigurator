<template>
    <div class="footer-container">
        <el-footer class="footer">
            <div class="footer-container">
                <span>QChatGPT快速上手配置页 ©2019 Created by <a href="https://space.bilibili.com/407410594">UP主：TheLazy</a> </span>
            </div>
        </el-footer>
    </div>
</template>

<script>
export default {
    name: 'FontEndAdminFooter',

    data() {
        return {
            
        };
    },
};
</script>

<style lang="css" scoped>
.footer-container {
    margin-top: 100px;
    bottom: 0;
    width: 100%;
    z-index: 999;
}
a{
    color: #409EFF;
    text-decoration: none;
    font-weight: bolder
}
</style>