node {
    def image
    def image_test_name = "stone1231/jks_app_img:test"
    def image_name = "stone1231/jks_app_img:prd"
    def container_name = "jks_app"
    def port = 8000

    stage('Clone repository') {
        checkout scm
        // if(fileExists("myapp")){
        //     dir("myapp"){
        //         sh "git pull"
        //     }            
        // }
        // else{
        //     sh "git clone https://sy43:BGZE32gyZvNmLLJZbuvs@gitlab.newegg.org/sy43/myapp.git"         
        // }
    }

    stage('Build image') {
        image = docker.build("${image_test_name}")
        //image = docker.build("${image_test_name}", "-f app/Dockerfile .")
    }

    stage('Test image') {
        //sh "docker run --rm ${image_test_name} python -m unittest discover -v /app"
        try{
            image.inside {
                sh "python -m unittest discover -v /app"               
            }             
        } catch(Exception ex) {
            sh "docker rmi ${image_test_name}"
            throw ex
        }         
    }
    
    stage('Push image') { 
        remove_early(image_name,container_name)
        sh "docker image tag ${image_test_name} ${image_name}"
        sh "docker push ${image_name}"
        sh "docker rmi ${image_test_name}"
    }

    stage('Run server') {
        remove_early(image_name,container_name)
        sh "docker run -d -p ${port}:${port} --name ${container_name} ${image_name} python /app/app.py ${port}"        
    }
}

def remove_early(image_name, container_name){
    //sh "docker container ls | grep myapp && docker rm -f myapp"
    def check = sh returnStatus: true, script: "docker ps -a | grep \' ${container_name}\$\'"
    if(check ==0){
        //echo "has it"
        sh "docker rm -f ${container_name}"
    }

    check = sh returnStatus: true, script: "docker images | sed 's/  */:/g' | grep '^${image_name}:'"
    if(check ==0){
        //echo "has it"
        sh "docker rmi ${image_name}"
    }    
}