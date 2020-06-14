//var yeshuv_type = document.querySelector('#yeshuv_type').value

var yeshuv = document.querySelector('#total_yeshuv_json').value
var yeshuv_json = JSON.parse(yeshuv)


const error_vote_percent = 100*(yeshuv_json['22'][0]["Error_Voters"]/ yeshuv_json['22'][0]["Voters"])
const error_round = Math.round((error_vote_percent + Number.EPSILON) * 100) / 100


    var barChartData = {
    labels: ['Vote %', 'Avg BZB Per Kalfi',  'Error Vote %'],
    datasets: [{
        label: 'ממוצע ישוב',
        backgroundColor: 'rgb(255, 99, 132)',
        stack: 'Stack 0',
        yAxisID: 'y-axis-1',
        data: [
   yeshuv_json['22'][0]["vote_percent"],
        yeshuv_json['22'][0]["Avg_BZB"],
        error_round

        ]
    }, {
        label: 'ממוצע ארצי',
        backgroundColor: 'rgb(255, 99, 33)',
        stack: 'Stack 1',

        data: [
            65.53,
            606.43,
            0.68

        ]
    }, {
        label: 'ממוצע סוג ישוב',
        backgroundColor: 'rgb(32, 99, 33)',
        stack: 'Stack 2',
        data: [
            25.53,
            506.43,
            0.38

        ]
    }]

};


var config_compare_canvas = {
    type: 'bar',
    data: barChartData,
    options: {
        title: {
            display: true,
            text: 'השוואת נתוני ישוב לממוצע ארצי ולממוצע סוג ישוב'
        },
        tooltips: {
            mode: 'index',
            intersect: false
        },
        responsive: true,
        scales: {
            xAxes: [{
                stacked: true,
            }],
            yAxes: [{
                stacked: true
            }]
        }
    }
};


window.addEventListener('load', function() {
    var ctx = document.getElementById('compare_canvas');
    window.dd = Chart.Line(ctx, config_compare_canvas );
});

