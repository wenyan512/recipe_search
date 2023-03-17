
<template>
<div id="blur">
<section class="w3l-whyblock py-3">
    <el-container class="pb-lg-5 pb-md-4 pb-2">
        <el-header id="site-header" style="font-size: 30px; font-weight: bold;">
            <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light">
                <a class="navbar-brand" style="color:grey;">
                    <i class="el-icon-dish"></i>Cooking 
                </a>   
            </nav>
        </div>                   
        </el-header>
        <div class="row align-items-center m-0">
            <div class="col-lg-6 ps-0" style="margin-left:6%;">
                <el-row>
                    <el-col :span=12>
                        <h4 class="title-style mb-4" style="float:center;font-weight:bold;color:darkred">No-Bake Nut Cookies</h4>
                        
                        <img src="../assets/images/rocky-road-cake.jpg"></el-col>
                    <el-col :span=12>
                        <h5 style="color:crimson; font-weight: bold;">Ingredients: </h5> <br/>
                        <li style="text-align: left;"> <i class="el-icon-star-off"></i>  1 c. firmly packed brown sugar</li>
                            <li style="text-align: left;"><i class="el-icon-star-off"></i>  1/2 c. evaporated milk</li>
                            
                                <li style="text-align: left;"><i class="el-icon-star-off"></i> 1/2 tsp. vanilla</li> 
                                <li style="text-align: left;"><i class="el-icon-star-off"></i>  1/2 c. broken nuts...</li>
                
                    </el-col>
                   
                </el-row> <el-divider></el-divider>
                <div class="two-grids mt-3">
                    <h5 style="color:crimson">Descriptions</h5> <br/>
                    <div class="grids_info">
                        <i class="el-icon-star-off"></i>
                        <div class="detail">
                            
                            <p>Grease and flour 12-cup fluted tube pan or Bundt pan. In small bowl, mix walnuts, raisins, marshmallows and chocolate pieces.</p>
                        </div>
                    </div>
                    <div class="grids_info mt-xl-5 mt-lg-4 mt-5">
                        <i class="el-icon-star-off"></i>
                        <div class="detail">
                            <p>Grease and flour 12-cup fluted tube pan or Bundt pan. In small bowl, mix walnuts, raisins, marshmallows and chocolate pieces.</p>
                        </div>
                    </div>
                    <div class="grids_info mt-xl-5 mt-lg-4 mt-5">
                        <i class="el-icon-star-off"></i>
                        <div class="detail">
                     
                            <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
                                mollit.</p>
                        </div>
                    </div>
                </div>
                
            </div>
            <div class="col-lg-5 ps-xl-5 ps-lg-4 mt-lg-0 mt-5">
                <div class="login_box">
                    <h4 style="float:center;font-weight:bold;color:grey">Create New Search</h4>
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
</el-container>
</section>
</div>
</template>

<script>// @ts-nocheck

export default{
    name:"Detail",
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
                            this.$message.success("为您推荐以下景点：）")
                            this.$router.push({
                                name: 'SearchResult', 
                                params: {
                                    dish: this.searchForm.dish,
                                    ingredient: this.searchForm.ingredient,
                                    include: this.searchForm.include,
                                    exclude: this.searchForm.exclude,
                                }
                            });
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
img{
    max-width: 80%;
    height: auto;
}
#blur{
    z-index:0;
    height: 100%;
    background: rgba(251,235,235,.4); 
}
.el-form-item__content {
  display: flex;
  align-items: center;
}
.login_box{
    width: 75%;
    height: 100%;
    background-color: #ffffff;
    background: rgba(255, 255, 255, 0.6);
    z-index:1;
    opacity: 0.9;
    filter: alpha(opacity=90);
    border-radius: 20px;
    border:1px solid #ffffff;
    text-align: center;
    margin-left: 50%;
    margin-top:60%;
    padding-top: 5%;
    padding-bottom:5%;
    transform: translate(-50%,-50%);
    
}
</style>
