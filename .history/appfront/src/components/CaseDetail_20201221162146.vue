<template>
<div class="case_detail">
    <detail-data v-bind:detailData = "detailData"></detail-data>
    <!--
    <el-row>
        <el-table :data="detail">
            <el-table-column prop="name" label="名称">
                <template v-slot:default="scope">
                {{ scope.row.fields.case_name }}
                </template>
            </el-table-column>
            <el-table-column prop="method" label="方式">
                <template v-slot:default="scope">
                {{ scope.row.fields.case_method }}
                </template>
            </el-table-column>
            <el-table-column prop="url" label="地址">
                <template v-slot:default="scope">
                {{ scope.row.fields.case_url }}
                </template>
            </el-table-column>
        </el-table>
    </el-row>
    -->
    <table style="width: 100%" class="myTable">
        <template v-for="(item, index) in detail">
            <router-link :key="index" :to="{name:'EditCase', params:{id: item.pk}}"><span>edit</span></router-link>
        <tr :key="index">
            <td class="column">名称</td>
            <td class="column">{{ item.fields.case_name }}</td>
        </tr>
        <tr :key="index">
            <td class="column">method</td>
            <td class="column">{{ item.fields.case_method }}</td>
        </tr>
        <tr :key="index">
            <td class="column">url</td>
            <td class="column">{{ item.fields.case_url }}</td>
        </tr>
        <tr :key="index">
            <td class="column">body</td>
            <td class="column">{{ item.fields.case_body }}</td>
        </tr>
        <tr :key="index">
            <td class="column">assert</td>
            <td class="column">{{ item.fields.case_assert }}</td>
        </tr>
        <tr :key="index">
            <td class="column">add_time</td>
            <td class="column">{{ item.fields.case_add_time }}</td>
        </tr>
        <tr :key="index">
            <td class="column">file_path</td>
            <td class="column">{{ item.fields.case_file_path}}</td>
        </tr>
        
        </template>
        
    </table>
</div>

</template>

<style>
.myTable {
  border-collapse: collapse;
  margin: 0 auto;
  text-align: center;
}
 
.myTable td,
.myTable th {
  border: 1px solid #cad9ea;
  color: #666;
  height: 60px;
}
</style>

<script>
import EditCase from "@/components/EditCase.vue";
export default {
    
    name: 'case_detail',
    data() {
        return {
            detail: this.detail,
            caseList: this.detail,
        }
    },
    conponents: { EditCase },
    mounted: function(){
        this.show_case_detail()
    },
    methods: {
        show_case_detail() {
            this.$http.get('http://127.0.0.1:8000/api/case_detail/'+this.$route.params.id)
                .then(response => {
                    var res = JSON.parse(response.bodyText)
                    console.log(res)
                    if (res['code'] == 0) {
                        this.detail = res['msg']
                        console.log(res['msg'])
                        //document.write(res)
                        
                    } else {
                        console.log(res['msg'])
                    }
                })
        },

        // edit_case() {
        //     this.$http.get('http://127.0.0.1:8000/api/edit_detail/'+ this.$route.params.id)
        // }
    }
}
</script>  