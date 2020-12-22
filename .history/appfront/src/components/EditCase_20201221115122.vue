<template>
<div class="editcase">

<form method="POST">
    <template v-for="(item,index) in caseForm">
        {{item}}
        <input :key="index" type="text" v-model="item">
    </template>
</form>
</template>

<script>
export default {
    name: "editcase",
    data () {
        return {
            caseForm : {
                "case_name": "name1",
                "case_method": "method",
                "case_url": "url",
                "case_body": "body",
                "case_assert": "assert",
                "case_file_path": "path"
            }
            //caseForm: this.caseForm
        }
    },
    // mounted: function(){
    //     this.getCase()
    // },
    // methods: {
    //     getCase() {
    //         this.$http.get('http://127.0.0.1:8000/api/case_detail/' + this.$route.params.id)
    //             .then(response => {
    //                 var res = JSON.parse(response.bodyText)
    //                 this.caseForm = res['msg']
    //                 //var caseData = formData
    //                 //caseData['case_name'] = formData['case_name']
    //                 console.log(res['msg'])
    //                 // console.log(caseData)
                    
    //             })
    //     }
    // }


}
</script>