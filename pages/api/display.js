const { spawn } = require('child_process');
let prcs = null;

export default async function handler(req, res) {
    if(req.method == 'GET'){
        if(prcs){
            res.status(200).json({ errCode: 1, message: 'Displayworker running' })
        }else{
            res.status(200).json({ errCode: 0, message: 'No displayworker running' })
        }

    }else if(req.method == 'POST'){

        const data = req.body;

        console.log(data);

        /* if(data.worker){
            if(!prcs){
                prcs = spawn('python', ['./display/driver.py', data.worker]);

                res.status(200).json({ errCode: 0, message: 'Started the displayworker!' })
            }else{
                res.status(200).json({ errCode: 1, message: 'Displayworker already running. Try killing the old one before starting a new one!' })
            }
        }else{
            res.status(400).json({ errCode: 2, message: 'Please provide the service to load!' })
        } */

        res.status(200).json({ errCode: 0, message: 'Started the displayworker!' })
        
    }else if(req.method == 'DELETE'){
        if(prcs){
            prcs.kill();
            prcs = null;
            res.status(200).json({ errCode: 0, message: 'Killed the displayworker!' });
        }else{
            res.status(400).json({ errCode: 0, message: 'No displayworker running!' });
        }
    }else{
        res.status(400).json({ errCode: -1, message: 'Method forbidden' })
    }
}
  