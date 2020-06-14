
var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
};


var test = document.querySelector('#kalfi_num').value
var yeshuv = document.querySelector('#total_yeshuv_json').value
alert(typeof(yeshuv))
var yeshuv_json = JSON.parse(yeshuv)

alert(obj['18'][0]["BZB"])
var color = Chart.helpers.color;
var config = {
               type: 'radar',
               data: {
                 labels: ["Kalfi #", "Vote %", "Error Vote %", "Student Loans", "Personal Loans"],
                 datasets: [

                 {
                       label: "lolw",
                       data: [test, 37, 2.7 ],
                     }


                 ],
               },
               options: {
                 tooltips: {
                   callbacks: {
                     label: function(tooltipItem, data) {
                       return data.datasets[tooltipItem.datasetIndex].label + ": " + tooltipItem.yLabel;
                     }
                   }
                 }
               }
             };



window.onload = function() {

var ctx = document.getElementById('aaacanvas');
    window.myRadar = new Chart(ctx, config);
};
