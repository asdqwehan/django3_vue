<template>
    <div class='home'>
    <el-row>
        <el-button type="primary" @click="testLogin()">测试</el-button>
    </el-row>
    <el-row>
      <el-button type="primary" @click="showCases()">显示</el-button>
      <el-table :data="caseList" >
          <el-table-column>
                <template scope="scope">
                    <router-link :to="{name: 'CaseDetail', params:{ id: scope.row.pk}}">this: {{ scope.row.fields.case_name}}</router-link>
                    <!--<router-link :to="{name:'CaseDetail',params:{ id:item.pk }}">this: {{ item.case_name }}</router-link>-->
                </template>
                
                <!--
                <div>
                    <router-link  scope="scope" :to="{name:'CaseDetail', params:{scope.row.pk}}"></router-link>
                </div>
                -->
                
          </el-table-column>
      </el-table>
    </el-row>
    </div>
</template>

<script>
export default {
    name: 'home',
    data() {
        return {
            caseList: this.caseList,
            list_1: [1,2,3,4]
        }
    },
    mounted: function() {
        this.showCases()
    },
    methods: {
        testLogin(){
            this.$http.get('http://127.0.0.1:8000/api/test_login')
                .then(response => {
                    var res = JSON.parse(response.bodyText)
                    console.log(res)
                    if (res['error_num'] == 0) {
                        this.$message.info('测试成功')
                    } else {
                        this.$message.error('测试失败')
                        console.log(res['msg'])
                    }
                })
        },

        showCases(){
            this.$http.get('http://127.0.0.1:8000/api/show_cases')
                .then(response => {
                    var res = JSON.parse(response.bodyText)
                    console.log(res['msg'])
                    if (res['code'] == 0) {
                        this.caseList = res['msg']
                        console.log(res['code'])
                        console.log(res['msg'])
                    } else {
                        console.log(res['msg'])
                    }
                })
        },
    }
}
</script>