/* app/static/js/scripts.js */
// JavaScript for handling chart rendering and other interactivity
document.addEventListener("DOMContentLoaded", function () {
    // Example of initializing a Chart.js chart
    var ctx1 = document.getElementById('population-trends').getContext('2d');
    var populationTrendsChart = new Chart(ctx1, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
                label: 'Vaches',
                data: [120, 125, 130, 128, 135],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }, {
                label: 'Cochons',
                data: [80, 82, 85, 83, 88],
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Repeat similar initialization for other charts
});
