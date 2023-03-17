<template>
    <div id="homepage">
        <div id="blur">
            <div class="banner-content">
                <div id="demo-1">
                    <div class="demo-inner-content text-center">
                        <div class="banner-info" style="margin-top:5%;">
                                <h5>Cooking is Easy</h5>
                                <h3 class="mt-2 mb-5">Passion For Cooking</h3>
                                <br/>
                        <div class="login_box">
                                <el-form :model="searchForm" :rules="searchrules" ref="searchForm" style="padding-top: 10%;">
                                    <el-form-item prop="dish" style="display: inline-block;">
                                        <el-input type="input" v-model="searchForm.dish" prefix-icon="el-icon-knife-fork" style="width: 300px; height: 40px; border-radius:30px 30px 30px 30px;" placeholder="Please input dish name" />
                                    </el-form-item>
                                    <el-form-item prop="ingredient" style="display: inline-block;">
                                        <el-input type="input" v-model="searchForm.ingredient" prefix-icon="el-icon-chicken" style="width: 300px; height: 40px;" placeholder="Must-have ingredients" />
                                    </el-form-item>
                                    <el-form-item prop="include" style="display: inline-block;">
                                        <el-input type="input" v-model="searchForm.include" prefix-icon="el-icon-question" style="width: 300px; height: 40px;" placeholder="May include ingredients" />
                                    </el-form-item>
                                    <el-form-item prop="exclude" style="display: inline-block;">
                                        <el-input type="input" v-model="searchForm.exclude" prefix-icon="el-icon-remove-outline" style="width: 300px; height: 40px;" placeholder="Ingredients to exclude" />
                                    </el-form-item>
                                    <br/>
                                    <el-form-item style="display: inline-block;">
                                        <el-button type="danger" size="large" style="width:200px;height: 40px;" @click="submitForm('searchForm')" round>Search</el-button>
                                    </el-form-item>
                                </el-form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>// @ts-nocheck
import axios from 'axios';
export default{
    name:"Homepage",
    data(){
        var vString=(rule, value, callback)=>{
            if (value == null || value == undefined || value == ""){
                callback()
            }
            else if (!(/\s*^[A-Za-z]/).test(value)){
                callback(new Error('Please enter string'))
            }
            else{
                callback()
            }
        }
        
        return{
            searchForm: {
                    dish: '',
                    ingredient: '',
                    include: '',
                    exclude: ''
                },
            searchrules: {
                    dish: [{ validator: vString, trigger: 'blur' },],
                    ingredient: [{ validator: vString, trigger: 'blur' },],
                    include: [{ validator: vString, trigger: 'blur' },],
                    exclude: [{ validator: vString, trigger: 'blur' },],
                }
        };
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    console.log(this.searchForm.dish)
                    if (this.searchForm.dish == '' && this.searchForm.ingredient == '' && this.searchForm.include == '' && this.searchForm.exclude == ""){
                        this.$message.error("Please enter at least one field!") 
                    }
                    else{
                        const path = 'http://127.0.0.1:5000/test';
                        axios.post(path,{
                            dish: this.searchForm.dish,
                            ingredient: this.searchForm.ingredient,
                            include: this.searchForm.include,
                            exclude: this.searchForm.exclude,
                        }).then((res)=>{
                            this.$message.success("为您推荐以下路线：）")
                            this.$router.push({
                                name: 'SearchResult', 
                                params: {
                                    title: res.data.title,
                                    ingredients: res.data.ingredients
                                }
                            })   
                            })
                    }
                } 
                else {
                    console.log('error submit!!');
                    return false;
                }
            });
        }

    },
}

</script>
<style src="../assets/style-starter.css">

</style>

<style>
#homepage{
    background:url("../assets/images/banner3.jpg");
    width:100%;
    height:100%;
    position:fixed;
    background-size:100% 100%;
}

#blur{
    height: 100%;
    background: rgba(0,0,0,.4); 
}

.el-form-item__content {
  display: flex;
  align-items: center;
}
.login_box{
    width: 400px;
    height: 350px;
    /* background-color: #ffffff; */
    background: rgba(255,255,255,0.3);
    opacity: 0.9;
    filter: alpha(opacity=90);
    border-radius: 20px;
    text-align: center;
    margin-left: 50%;
    margin-top: 15%;
    transform: translate(-50%,-50%);
    
}

</style>
