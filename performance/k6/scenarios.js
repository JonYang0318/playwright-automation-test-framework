export const smokeScenario = {

    executor: 'constant-vus',

    //  給CI Pipeline 使用 少量使用者快速驗證 API

    vus: 5,

    duration: '30s',

};



export const loadScenario = {

    executor: 'ramping-vus',

    startVUs: 0,


    // 模擬正常使用流量

    stages: [

        {
            duration: '30s',
            target: 20,
        },


        {
            duration: '1m',
            target: 50,
        },


        {
            duration: '30s',
            target: 0,
        },

    ],

};



export const stressScenario = {


    executor: 'ramping-vus',

    startVUs: 0,


    // 模擬高流量情境

    stages: [

        {
            duration: '30s',
            target: 50,
        },


        {
            duration: '1m',
            target: 100,
        },


        {
            duration: '30s',
            target: 0,
        },

    ],

};