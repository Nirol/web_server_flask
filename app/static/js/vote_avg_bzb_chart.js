var test = document.querySelector('#kalfi_num').value
var yeshuv = document.querySelector('#total_yeshuv_json').value
var yeshuv_json = JSON.parse(yeshuv)




var lineChartData = {
 labels: [['Knesset 18', 'February 10, 2009'], ['Knesset 19', 'January 22, 2013'], ['Knesset 20', 'March 17, 2015'], ['Knesset 21', 'April 9, 2019'], ['Knesset 22', 'September 17, 2019']],

    datasets: [{
        label: 'אחוז הצבעה',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        fill: false,
        data: [
        yeshuv_json['18'][0]["vote_percent"],
            yeshuv_json['19'][0]["vote_percent"],
            yeshuv_json['20'][0]["vote_percent"],
            yeshuv_json['21'][0]["vote_percent"],
            yeshuv_json['22'][0]["vote_percent"]
        ],
        yAxisID: 'y-axis-1',
    }, {
        label: 'מספר מצביעים ממוצע בקלפי',
        backgroundColor: 'rgb(176, 22, 132)',
        borderColor: 'rgb(176, 22, 132)',
        fill: false,
        data: [
             yeshuv_json['18'][0]["vote_percent"],
                     yeshuv_json['19'][0]["Avg_BZB"],
                     yeshuv_json['20'][0]["Avg_BZB"],
                     yeshuv_json['21'][0]["Avg_BZB"],
                     yeshuv_json['22'][0]["Avg_BZB"]

        ],
        borderDash: [5, 5],
        pointRadius: 7,
        pointHoverRadius: 10,
        yAxisID: 'y-axis-2'
    }]
};




var config_vote_p_avg_bzb_canvas = {
                     data: lineChartData,
                     options: {
                         responsive: true,
                         hoverMode: 'index',
                         stacked: false,
                         title: {
                             display: true,
                             text: 'אחוז הצבעה ומספר מצביעים ממוצע לקלפי'
                         },
                         scales: {

                         xAxes: [{
                               scaleFontSize: 10

                             }],
                             yAxes: [{
                                 type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                                 display: true,
                                 position: 'left',
                                 id: 'y-axis-1',
                                 scaleLabel: {
                                    display: true,
                                    labelString: 'Vote %'
                                }

                             }, {
                                 type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                                 display: true,
                                 position: 'right',
                                 id: 'y-axis-2',
                                 scaleLabel: {
                                    display: true,
                                    labelString: 'Kalfi Avg BZB'
                                },
                                 // grid line settings
                                 gridLines: {
                                     drawOnChartArea: false, // only want the grid lines for one axis to show up
                                 },
                             }],
                         }
                     }
                 };


window.addEventListener('load', function() {
    var ctx = document.getElementById('vote_p_avg_bzb_canvas');
    window.aa = Chart.Line(ctx, config_vote_p_avg_bzb_canvas );
});

