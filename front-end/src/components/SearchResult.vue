<template>
    <el-container class="w3l-courses py-5" id="courses" style="padding-bottom:3%;">
        <el-header id="site-header" style="font-size: 40px; font-weight: bold;">
            <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light">
                <el-row style="width:100%;">
                <el-form :model="searchForm" :rules="searchrules" ref="searchForm" class="d-flex search-header">
                    <el-col :span=4 class="navbar-brand" style="color:grey;">
                        <i class="el-icon-dish"></i>
                        Cooking
                    </el-col>
                    <el-col :span=8 >
                        <el-form-item>
                            <input class="form-control" type="input" style="width:80%;" v-model="searchForm.dish" placeholder="Add any" aria-label="Search" />
                        </el-form-item>
                    </el-col>
                <el-col :span=8>
                    <el-form-item>
                            <input class="form-control" type="search" style="width:80%;" v-model="searchForm.exclude" placeholder="Enter Keyword..." aria-label="Search" />
                        
                   </el-form-item>
                </el-col>
                <el-col :span=2 >
                    <el-form-item>
                <el-button class="btn btn-style" type="submit"><i class="fas fa-search"></i></el-button></el-form-item>
            </el-col>
            </el-form>
                <!-- toggle switch for light and dark theme -->
                <!-- //toggle switch for light and dark theme -->
            </el-row>
            </nav>
        </div>                   
        </el-header>
        <div class="container py-lg-5 py-md-4 py-2">
            <div class="row justify-content-center">
                <div class="col-lg-4 col-md-6 item mt-5">
                    <el-card class="card">
                        <div class="card-header p-0 position-relative">
                            <a class="zoom d-block">
                                <img class="card-img-bottom d-block" src="../assets/images/rocky-road-cake.jpg" alt="Card image cap">
                            </a>
                            <div class="post-pos">
                                <a  class="receipe blue">Beginner</a>
                                <a  class="receipe yellow ml-2">{{title}}</a>
                            </div>
                        </div>
                        <div class="card-body course-details">
                            <a class="course-desc">How to make singapore chicken rise at home
                            </a>
                            <div class="course-meta mt-4">
                                <div class="meta-item course-lesson">
                                    <span class="meta-value"> 68 Students enrolled</span>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
                <div class="col-lg-4 col-md-6 item mt-5">
                    <el-card class="card">
                        <div class="card-header p-0 position-relative">
                            <a class="zoom d-block">
                                <img class="card-img-bottom d-block" src="../assets/images/c1.jpg" alt="Card image cap">
                            </a>
                            <div class="post-pos">
                                <a  class="receipe blue">Beginner</a>
                                <a  class="receipe yellow ml-2">New</a>
                            </div>
                        </div>
                        <div class="card-body course-details">
                            <a class="course-desc">How to make singapore chicken rise at home
                            </a>
                            <div class="course-meta mt-4">
                                <div class="meta-item course-lesson">
                                    <span class="meta-value"> 68 Students enrolled</span>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
                <div class="col-lg-4 col-md-6 item mt-5">
                    <el-card class="card">
                        <div class="card-header p-0 position-relative">
                            <a class="zoom d-block">
                                <img class="card-img-bottom d-block" src="../assets/images/c1.jpg" alt="Card image cap">
                            </a>
                            <div class="post-pos">
                                <a  class="receipe blue">Beginner</a>
                                <a  class="receipe yellow ml-2">New</a>
                            </div>
                        </div>
                        <div class="card-body course-details">
                            <a class="course-desc">How to make singapore chicken rise at home
                            </a>
                            <div class="course-meta mt-4">
                                <div class="meta-item course-lesson">
                                    <span class="meta-value"> 68 Students enrolled</span>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
                <div class="col-lg-4 col-md-6 item mt-5">
                    <el-card class="card">
                        <div class="card-header p-0 position-relative">
                            <a class="zoom d-block">
                                <img class="card-img-bottom d-block" src="../assets/images/c1.jpg" alt="Card image cap">
                            </a>
                            <div class="post-pos">
                                <a  class="receipe blue">Beginner</a>
                                <a  class="receipe yellow ml-2">New</a>
                            </div>
                        </div>
                        <div class="card-body course-details">
                            <a class="course-desc">How to make singapore chicken rise at home
                            </a>
                            <div class="course-meta mt-4">
                                <div class="meta-item course-lesson">
                                    <span class="meta-value"> 68 Students enrolled</span>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
                <div class="col-lg-4 col-md-6 item mt-5">
                    <el-card class="card">
                        <div class="card-header p-0 position-relative">
                            <a class="zoom d-block">
                                <img class="card-img-bottom d-block" src="../assets/images/c1.jpg" alt="Card image cap">
                            </a>
                            <div class="post-pos">
                                <a  class="receipe blue">Beginner</a>
                                <a  class="receipe yellow ml-2">New</a>
                            </div>
                        </div>
                        <div class="card-body course-details">
                            <a class="course-desc">How to make singapore chicken rise at home
                            </a>
                            <div class="course-meta mt-4">
                                <div class="meta-item course-lesson">
                                    <span class="meta-value"> 68 Students enrolled</span>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
                <div class="col-lg-4 col-md-6 item mt-5">
                    <el-card class="card">
                        <div class="card-header p-0 position-relative">
                            <a class="zoom d-block">
                                <img class="card-img-bottom d-block" src="../assets/images/c1.jpg" alt="Card image cap">
                            </a>
                            <div class="post-pos">
                                <a  class="receipe blue">Beginner</a>
                                <a  class="receipe yellow ml-2">New</a>
                            </div>
                        </div>
                        <div class="card-body course-details">
                            <a class="course-desc">How to make singapore chicken rise at home
                            </a>
                            <div class="course-meta mt-4">
                                <div class="meta-item course-lesson">
                                    <span class="meta-value"> 68 Students enrolled</span>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </div>
                    </div>
        </div>
  
            <!-- pagination -->
            <div class="pagination-wrapper mt-5 pt-lg-3 text-center">
                <ul class="page-pagination">
                    <li><span aria-current="page" class="page-numbers current">1</span></li>
                    <li><a class="page-numbers" href="#url">2</a></li>
                    <li><a class="page-numbers" href="#url">3</a></li>
                    <li><a class="page-numbers" href="#url">...</a></li>
                    <li><a class="page-numbers" href="#url">15</a></li>
                    <li><a class="next">Next</a></li>
                </ul>
            </div>
            <!-- //pagination -->
    </el-container>
</template>

<script>
export default{
    name:"SearchResult",
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
                    exclude: '',
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

    },
    created(){
        this.title = this.$route.params.title;
        this.ingredients = this.$route.params.ingredients;
        console.log(this.title);
        
    }

}

</script>
<style src="../assets/style-starter.css">

</style>

<style scoped>
:deep() .el-input__inner{   /*或者 .s2>>>.el-input__inner  */
    border-radius: 20px;    /*输入框圆角值*/
  }
</style>
<style>
#blur{
    height: 100%;
    background: rgba(0,0,0,.4); 
}

.el-form-item__content {
  display: flex;
  align-items: center;
}

</style>
