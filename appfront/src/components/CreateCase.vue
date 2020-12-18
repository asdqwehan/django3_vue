<template>
<div class="form_box">
    <form action="" method="POST">
        <input type="text" name="name" value="name" v-model="createForm.case_name">
        <input type="text" v-model="createForm.case_method">
        <input type="text" v-model="createForm.case_url" placeholder="请输入url">
        <input type="text" v-model="createForm.case_body" placeholder="请输入body">
        <input type="text" v-model="createForm.case_assert" placeholder="请输入assert">
        <input type="text" v-model="createForm.case_file_path" placeholder="请输入file_path">
        <el-button type="submit" @click="onSubmit($event)">提交</el-button>
    </form>
</div>
</template>

<script>
export default {
    name: "form",
    data () {
        return {
            createForm: {
                "case_name": "name1",
                "case_method": "",
                "case_url": "",
                "case_body": "",
                "case_assert": "",
                "case_file_path": ""

            }
        }
    },
    methods: {
        onSubmit(event) {
            //event.preventDefault() //阻止行为
            let formData = JSON.stringify(this.createForm);
            console.log(formData)
            this.$http.post('http://127.0.0.1:8000/api/create_case',formData) //post(url, formdata)
                .then(response => {
                    var res = JSON.parse(response.bodyText)
                    console.log(res)
                    if (res['code'] == 0){
                        console.log(res['msg'])
                        this.$router.push('/') //跳转
                    } else{
                        console.log(res['msg'])
                    }
                })
                    
        }
    }
}
</script>