<template>
    <div id="homepage">
        <div id="blur">
            <div class="banner-content">
                <div id="demo-1">
                    <div class="demo-inner-content text-center">
                        <el-row class="banner-info" style="margin-top:6%;">
                                <h5>Cooking is Easy</h5>
                                <h3>Passion For Cooking</h3>
                              
                            </el-row>
                        <el-row>
                                <el-form :model="searchForm" :rules="searchrules" ref="searchForm">
                                    <el-form-item prop="dish" style="display: inline-block;">
                                        <el-input v-show="!suggest" type="input" v-model="searchForm.dish" prefix-icon="el-icon-knife-fork" style="width: 300px; height: 40px; border-radius:30px 30px 30px 30px;" placeholder="Please input query" />
                                            <el-autocomplete 
                                                v-show="suggest"
                                                class="inline-input"
                                                v-model="searchForm.dish"
                                                :fetch-suggestions="focusInput"
                                                placeholder="Please input query"
                                                prefix-icon="el-icon-knife-fork"
                                                style="width: 300px; height: 40px; border-radius:30px 30px 30px 30px;"
                                                :trigger-on-focus="false"
                                                @select="handleSelect"
                                            >
                                            </el-autocomplete>
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
                                        <el-switch
                                    style="display: block"
                                    v-model="value"
                                    active-color="#13ce66"
                                    inactive-color="#ff4949"
                                    active-text="Search dish"
                                    inactive-text="Search directions"
                                    activate-value="dish"
                                    inactivate-text="directions"
                                    @change="changeStatus">
                                    </el-switch>
                                    </el-form-item>
                                    <el-form-item style="display: inline-block;">
                                       
                                        <el-button type="danger" size="large" style="width:200px;height: 40px;" @click="submitForm('searchForm')" round>Search</el-button>
                                    </el-form-item>
                                </el-form>
        
                            </el-row>
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
            value: true,
            searchType: 'dish',
            suggestion: [],
            showSuggestion: false,
            listIndex: -1,
            suggest: true,
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
                            searchType: this.searchType,
                        }).then((res)=>{
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
        },
        changeStatus: function(callback){
            console.log(callback);
            if (callback==true){
                this.searchType = 'dish'
                this.suggest = true
            }
            else{
                this.searchType = 'directions'
                this.suggest = false
            }
            console.log(this.searchType);
        },
        focusInput(queryString, cb){
            if(this.searchType=='dish'){
                if (queryString && queryString.length>0){
                    const path = 'http://127.0.0.1:5000/suggestion';
                    axios.post(path,{
                        input: this.searchForm.dish
                    }).then((res)=>{
                        this.suggestion = res.data.suggestion

                        let result = this.suggestion.filter(dish => dish.indexOf(queryString) > -1)
                        console.log(result);
                        let suggestion = []
                        for (let i=0; i<result.length;i++){
                            console.log(result[i])
                             suggestion.push({
                                "value":result[i],
                                "address": ''});
                        }
                        console.log(result)
                        console.log(suggestion)
                        cb(suggestion);
                    })
                }
                else{
                    this.showSuggestion = false
                }
            }
        },
        handleSelect(item) {
            console.log(item);
        }
    },
    // watch: {
    //     'searchForm.dish': {
    //         handler: function() {
    //             console.log(this.searchForm.dish)
    //             if (this.searchForm.dish==''){
                    
    //                 this.showSuggestion = false
    //                 console.log(this.showSuggestion)
    //             }
    //             else{
    //                 this.focusInput()
    //             }
    //         }
    //     }
    // },
}

</script>
<style src="../assets/style-starter.css">

</style>

<style>
.el-row {
    margin-bottom: 10px;
  }

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

.el-form{
    width: 400px;
    height: auto;
    background: rgba(255,255,255,0.6);
    opacity: 0.9;
    filter: alpha(opacity=90);
    border-radius: 20px;
    text-align: center;
    margin-left: 50%;
    margin-top: 15%;
    padding-top: 3%;
    transform: translate(-50%,-50%);
    position: relative; 
}

.login_box{
    width: 400px;
    height: 400px;
    /* background-color: #ffffff; */
    background: rgba(255,255,255,0.6);
    opacity: 0.9;
    filter: alpha(opacity=90);
    border-radius: 20px;
    text-align: center;
    margin-left: 50%;
    margin-top: 10px;
    transform: translate(-50%,-50%);
    
}
/* .el-switch__label{
    color:crimson !important;
} */

.el-switch__label.el-switch__label--left.is-active{
    color:crimson !important;
}
.el-switch__label.el-switch__label--right.is-active{
    color:crimson !important;
}
</style>
