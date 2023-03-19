<template>
 <div id="blur">
    <el-container class="w3l-courses py-5" id="courses" style="padding-bottom:3%;">
        <el-header id="site-header" style="font-weight: bold;">
                    <nav class="navbar navbar-expand-lg navbar-light">
                        <a class="navbar-brand" style="color:grey; font-size: 25px;">
                            <i class="el-icon-back" @click="backhome()">Home </i>
                                <!-- <div class="headIcon" @click="backhome()">
                                </div> -->
                       </a>   
                    </nav>
               
            </el-header>
        <div class="container py-lg-0 py-md-0 py-0">
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
    </div>
</template>

<script>// @ts-nocheck

export default{
    name:"SearchResult",
    data(){
        return{
            recipes: [],
        };
    },
    methods: {

    },
    created(){
        this.title = this.$route.params.title;
        this.ingredients = this.$route.params.ingredients;
        this.recipes = this.$route.params.recipes;
        console.log(this.title);
    }

}

</script>
<style src="../assets/style-starter.css">

</style>

<style>
 #blur{
        height: 100%;
        background: rgba(251,235,235,.4); 
    }
.el-form-item__content {
  display: flex;
  align-items: center;
}

</style>
