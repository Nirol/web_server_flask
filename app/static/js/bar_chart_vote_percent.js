const yeshuv = document.querySelector('#total_yeshuv_json').value
const yeshuv_json = JSON.parse(yeshuv)

const yeshuv_name =document.querySelector('#yeshuv_name').value
const yeshuv_type = document.querySelector('#yeshuv_type').value
const yeshuv_type_json = JSON.parse(yeshuv_type)

const total_country = "ארצי"


const barChartData_vp = {
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
           yeshuv_json['22'][0]["vote_percent"],
            yeshuv_type_json["type_vote_percent"],
             65.53


        ]

    }]
};



var config_vp_canvas = {

  type: 'bar',
        data: barChartData_vp,
        options: {
            responsive: true,
 legend: {
        display: false
    },
            title: {
                display: true,
                text: 'אחוז הצבעה'
            },
            scales: {

yAxes: [{
                                    display: true,
                                    ticks: {
                                        suggestedMin: 0, //min
                                        suggestedMax: 100 //max
                                    }
                                }]
            }
        }
    }