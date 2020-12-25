
<template>
<div class="editcase">
            this:


<el-form method="POST">

        <el-input :key="index" type="text" v-model="caseForm.case_name"></el-input>
        <el-input :key="index" type="text" v-model="caseForm.case_method"></el-input>
        <el-input :key="index" type="text" v-model="caseForm.case_url"></el-input>
        <el-input :key="index" type="text" v-model="caseForm.case_assert"></el-input>
        <el-input :key="index" type="text" v-model="caseForm.case_body"></el-input>
        <el-input :key="index" type="text" v-model="caseForm.case_file_path"></el-input>
    <el-button type="submit" @click="onSubmit($event)">编辑</el-button>
</el-form>
</div>
</template>

<script>
export default {
    //props: {detailData: Array},
    // props: ["detailData"],
    name: "editcase",
    data () {
        return {
            caseForm : {}
            
        }
    },
    mounted: function(){
        // this.init(),
        this.getCase()
    },
    methods: {
        getCase() {
            this.$http.get('http://127.0.0.1:8000/api/case_detail/' + this.$route.params.id)
                .then(response => {

                    var res = JSON.parse(response.bodyText)
                    var caseForm = res['msg']
                    //var caseData = formData
                    //caseData['case_name'] = formData['case_name']
                    console.log(caseForm[0]['fields'])
                    this.caseForm = caseForm[0]['fields']
                    // console.log("data--:" + caseForm)
                    // console.log("this--:" + caseForm.fields.case_name)
                    // console.log(caseData)


                    
                })
        },

        // init() {
        //     var dataList = this.detailData
        //     console.log('this:--' + dataList)
        // },

        onSubmit(event) {
            event.preventDefault()
            let formData = JSON.stringify(this.caseForm)
            console.log(this.$route.params.id)
            this.axios.post('http://127.0.0.1/api/edit_case/' + this.$route.params.id, formData, {headers: { 'Content-Type': 'application/x-www-form-urlencoded'}})
                .then(response => {
                    var res = JSON.parse(response.bodyText)
                    console.log(res['msg'])
                })
        }
    }


}
</script>