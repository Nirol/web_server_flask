const yeshuv = document.querySelector('#total_yeshuv_json').value
const yeshuv_json = JSON.parse(yeshuv)

const error_vote_percent = 100*(yeshuv_json['22'][0]["Error_Voters"]/ yeshuv_json['22'][0]["Voters"])
const error_round = Math.round((error_vote_percent + Number.EPSILON) * 100) / 100

const yeshuv_name =document.querySelector('#yeshuv_name').value
const yeshuv_type = document.querySelector('#yeshuv_type').value
const yeshuv_type_json = JSON.parse(yeshuv_type)

const total_country = "ארצי"


const barChartData_evp = {
    labels: [yeshuv_name, yeshuv_type_json["type_name"], total_country],
    datasets: [{
        barPercentage: 0.1,
        categoryPercentage: 0.1,
        maxBarThickness: 8,
        barThickness: 6,
        backgroundColor: 'rgba(176, 22, 132, 0.4)',
        borderColor: 'rgba(176, 22, 132,0.9)',
        borderWidth: 3,
        hoverBackgroundColor: 'rgba(18, 195, 166, 0.4)' ,
        hoverBorderColor:  'rgba(18, 195, 166,0.9)',

        data: [
          error_round,
          yeshuv_type_json["type_error_vote_percent"],
          0.63


        ]

    }]
};


var config_evp_canvas = {

   type: 'bar',
        data: barChartData_evp,
        options: {
            responsive: true,
 legend: {
        display: false
    },
            title: {
                display: true,
                text: 'אחוז הצבעה שגויה'
            },
            scales: {

yAxes: [{
                                    display: true,
                                    ticks: {
                                        suggestedMin: 0, //min
                                        suggestedMax: 3 //max
                                    }
                                }]
            }
        }
    }


