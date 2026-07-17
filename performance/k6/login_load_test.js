import http from 'k6/http';

import {
    check,
    sleep
} from 'k6';


import {
    loadScenario
} from './scenarios.js';



export const options = {

    scenarios: {

        login_test: loadScenario

    },


    thresholds: {

        // 95% request response time 小於 2 秒

        http_req_duration:[
            'p(95)<2000'
        ],


        // error rate 小於 5%

        http_req_failed:[
            'rate<0.05'
        ]

    }

};



export default function(){


    const response = http.post(

        'http://127.0.0.1:8000/login',

        JSON.stringify({

            username: 'test_user',

            password: 'password123'

        }),

        {

            headers:{

                'Content-Type':
                'application/json'

            }

        }

    );



    check(response, {


        // HTTP Status 驗證

        'status is 200':
        (r)=>r.status === 200,


        // 驗證登入成功有 token

        'has token':
        (r)=>r.body && r.json('token') !== undefined,


        // 基本效能驗證

        'response time < 2s':
        (r)=>r.timings.duration < 2000


    });



    sleep(1);

}