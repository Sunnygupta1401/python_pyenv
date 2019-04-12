node{

stage('git checkout')
{

      checkout scm

}

 stage('python')
   {
    withPythonEnv('python') {
          
    sh 'pip install pytest'
    sh 'pytest'
    
    }  
      
   }

}
