<template>
<div class="editcase">
        <template >
            <form action="" method="POST" v-for="(item, index) in caseForm" :key="index">

                <input type="text" v-model="caseForm.case_name">
                

            </form>
        </template>

</template>

<script>
export default {
    name: "editcase",
    data () {
        return {
            caseForm : {
                "case_name": "name1",
                "case_method": "",
                "case_url": "",
                "case_body": "",
                "case_assert": "",
                "case_file_path": ""
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