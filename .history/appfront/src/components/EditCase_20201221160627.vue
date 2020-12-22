<template>
<div class="editcase">

<el-form method="POST">

        <el-input :key="index" type="text" v-model="caseForm.case_name"></el-input>
        
</el-form>
</template>

<script>
export default {
    props: ['detailData'],
    name: "editcase",
    data () {
        return {
            caseForm : {
                "case_name": "",
                "case_method": "",
                "case_url": "",
                "case_body": "",
                "case_assert": "",
                "case_file_path": ""
            },
            dataList: [],
        }
    },
    mounted: function(){
        this.getCase()
    },
    methods: {
        getCase() {
            this.$http.get('http://127.0.0.1:8000/api/case_detail/' + this.$route.params.id)
                .then(response => {
                    var res = JSON.parse(response.bodyText)
                    this.caseForm = res['msg']
                    //var caseData = formData
                    //caseData['case_name'] = formData['case_name']
                    console.log(res['msg'])
                    // console.log(caseData)
                    
                })
        },

        init() {
            this.dataList = this.detailData
        },
    }


}
</script>