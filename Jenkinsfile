node{

stage('git checkout')
{

      checkout scm

}

 stage('python')
   {
    withPythonEnv('python') {
          
    sh 'pip install pytest'
        sh 'pip install mock'
          sh 'pip install pytest_mock'

    sh 'pytest'
          
          sh 'which pytest'
    
    }  
      
   }

}
